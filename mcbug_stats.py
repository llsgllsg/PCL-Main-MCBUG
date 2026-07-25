import requests
import time
from datetime import datetime, timezone, timedelta
import os

def get_issue_count(jql: str, project: str = "MC", max_retries=3) -> int:
    url = "https://bugs.mojang.com/api/jql-search-post"
    page = 0
    page_size = 50
    total = 0

    while True:
        payload = {
            "advanced": True,
            "search": jql,
            "maxResults": page_size,
            "startAt": page * page_size
        }
        if project:
            payload["project"] = project

        for attempt in range(max_retries):
            try:
                resp = requests.post(url, json=payload, timeout=10)
                resp.raise_for_status()
                data = resp.json()
                issues = data.get("issues", [])
                total += len(issues)

                pagination = data.get("pagination", {})
                if not pagination.get("hasNextPage", False):
                    return total
                page += 1
                break
            except Exception as e:
                print(f"请求失败 (尝试 {attempt+1}/{max_retries}): {e}")
                time.sleep(2)
        else:
            print("重试次数用尽，放弃")
            return -1

def get_recently_fixed(project: str, limit=10, max_retries=3):
    url = "https://bugs.mojang.com/api/jql-search-post"
    jql = "fixVersion is not empty AND resolutiondate >= -7d"
    payload = {
        "advanced": True,
        "search": jql,
        "maxResults": limit,
        "project": project
    }

    for attempt in range(max_retries):
        try:
            resp = requests.post(url, json=payload, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            issues = data.get("issues", [])
            if issues:
                result = []
                for issue in issues:
                    key = issue.get("key")
                    fields = issue.get("fields", {})
                    summary = fields.get("summary", "无摘要")
                    status = fields.get("status", {}).get("name", "未知")
                    resolutiondate = fields.get("resolutiondate", "")
                    labels = fields.get("labels", [])
                    result.append({
                        "key": key,
                        "summary": summary,
                        "status": status,
                        "resolutiondate": resolutiondate,
                        "labels": labels
                    })
                if result and result[0]["resolutiondate"]:
                    result.sort(key=lambda x: x["resolutiondate"], reverse=True)
                return result
            else:
                if " -7d" in jql:
                    print(f"{project}: -7d 无数据，尝试 -24h")
                    return get_recently_fixed(project, limit, days="24h")
                return []
        except Exception as e:
            print(f"请求失败 (尝试 {attempt+1}/{max_retries}): {e}")
            time.sleep(2)
    return []

def generate_xaml(results, recent_mc, recent_mcpe, timestamp):
    project_names = {"MC": "Java版", "MCPE": "基岩版"}

    def build_stat_groupboxes():
        boxes = ""
        for proj, (created, resolved) in results.items():
            display = project_names.get(proj, proj)
            c_str = str(created) if created >= 0 else "失败"
            r_str = str(resolved) if resolved >= 0 else "失败"
            boxes += f'                <GroupBox Header="{display} 新增" Content="{c_str}" />\n'
            boxes += f'                <GroupBox Header="{display} 修复" Content="{r_str}" />\n'
        return boxes

    def build_list_items(items, max_count=10):
        if not items:
            return f'        <local:MyListItem Margin="-5,2,-5,8" Title="暂无数据" Info="请稍后再试" Type="TextOnly" />\n'
        lines = ""
        count = 0
        for item in items:
            if count >= max_count:
                break
            safe_summary = item["summary"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            status = item.get("status", "未知")
            labels = item.get("labels", [])
            labels_str = ", ".join(labels) if labels else "无标签"
            info_text = f"{safe_summary} ({status}) | 标签: {labels_str}"
            info_escaped = info_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            lines += f'        <local:MyListItem Margin="-5,2,-5,8" Logo="pack://application:,,,/images/Blocks/CommandBlock.png" Title="{item["key"]}" Info="{info_escaped}" Type="Clickable" EventType="打开网页" EventData="{{variable:SourcePrefix:https://bugs.mojang.com/browse/}}{item["key"]}" />\n'
            count += 1
        return lines

    mc_list = build_list_items(recent_mc)
    mcpe_list = build_list_items(recent_mcpe)
    stat_boxes = build_stat_groupboxes()

    xaml = f'''<StackPanel xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:local="clr-namespace:PCL;assembly=Plain Craft Launcher 2">

    <local:MyHint 
        Text="数据来自 Mojira Public API&#x0a;统计时间：{timestamp} (UTC+8)" 
        Theme="Blue"
        Margin="0,0,0,15"
    />

    <local:MyHint Text="当前数据源：官方源 (bugs.mojang.com)" Margin="0,0,0,10" Theme="Blue" Visibility="{{variable:IsOfficial:Visible}}" />
    <local:MyHint Text="当前数据源：镜像源 (mojira.dev)" Margin="0,0,0,10" Theme="Yellow" Visibility="{{variable:IsMirror:Collapsed}}" />

    <local:MyCard Title="过去24小时新增与修复漏洞统计" Margin="0,0,0,15" CanSwap="True" IsSwapped="False">
        <StackPanel Margin="25,40,23,15">
            <WrapPanel>
{stat_boxes}
            </WrapPanel>
            <TextBlock TextWrapping="Wrap" Margin="0,15,0,0" FontSize="11" Foreground="{{DynamicResource ColorBrush5}}"
                       Text="由于 API 缓存原因，数据可能有 5-30 分钟的延迟。" />
        </StackPanel>
    </local:MyCard>

    <local:MyCard Title="最新修复的漏洞 (Java版)" Margin="0,0,0,15" CanSwap="True" IsSwapped="True">
        <StackPanel Margin="25,40,23,15">
            <local:MyHint Text="点击列表项可直接跳转到对应的漏洞页面" Theme="Blue" Margin="0,0,0,10" />
            <StackPanel>
{mc_list}
            </StackPanel>
        </StackPanel>
    </local:MyCard>

    <local:MyCard Title="最新修复的漏洞 (基岩版)" Margin="0,0,0,15" CanSwap="True" IsSwapped="True">
        <StackPanel Margin="25,40,23,15">
            <local:MyHint Text="点击列表项可直接跳转到对应的漏洞页面" Theme="Blue" Margin="0,0,0,10" />
            <StackPanel>
{mcpe_list}
            </StackPanel>
        </StackPanel>
    </local:MyCard>

    <local:MyCard Title="操作" Margin="0,0,0,15" CanSwap="False">
        <StackPanel Margin="25,20,23,20" HorizontalAlignment="Center" Orientation="Horizontal">
            <local:MyButton Height="35" Padding="20,0,20,0" ColorType="Highlight"
                Text="切换到官方源">
                <local:CustomEventService.Events>
                    <local:CustomEventCollection>
                        <local:CustomEvent Type="修改变量" Data="SourcePrefix|https://bugs.mojang.com/browse/|-" />
                        <local:CustomEvent Type="修改变量" Data="IsOfficial|Visible|-" />
                        <local:CustomEvent Type="修改变量" Data="IsMirror|Collapsed|-" />
                        <local:CustomEvent Type="刷新页面" Data="-" />
                    </local:CustomEventCollection>
                </local:CustomEventService.Events>
            </local:MyButton>
            <local:MyButton Height="35" Padding="20,0,20,0" Margin="15,0,0,0"
                Text="切换到镜像源">
                <local:CustomEventService.Events>
                    <local:CustomEventCollection>
                        <local:CustomEvent Type="修改变量" Data="SourcePrefix|https://mojira.dev/|-" />
                        <local:CustomEvent Type="修改变量" Data="IsOfficial|Collapsed|-" />
                        <local:CustomEvent Type="修改变量" Data="IsMirror|Visible|-" />
                        <local:CustomEvent Type="刷新页面" Data="-" />
                    </local:CustomEventCollection>
                </local:CustomEventService.Events>
            </local:MyButton>
        </StackPanel>
    </local:MyCard>

</StackPanel>'''
    return xaml

def main():
    tz_utc8 = timezone(timedelta(hours=8))
    now = datetime.now(tz_utc8).strftime("%Y-%m-%d %H:%M:%S")
    print(f"统计时间 (UTC+8): {now}\n")

    projects = ["MC", "MCPE"]
    created_jql = "created >= -24h"
    resolved_jql = "resolutiondate >= -24h"

    results = {}
    for proj in projects:
        print(f"正在统计 {proj} 项目...")
        created = get_issue_count(created_jql, project=proj)
        resolved = get_issue_count(resolved_jql, project=proj)
        results[proj] = (created, resolved)

    print("\n正在获取最新修复的漏洞 (MC)...")
    recent_mc = get_recently_fixed("MC", limit=10)
    print("正在获取最新修复的漏洞 (MCPE)...")
    recent_mcpe = get_recently_fixed("MCPE", limit=10)

    print("\n=== 过去24小时统计 ===")
    print(f"{'项目':<8} {'新增':>8} {'修复':>8}")
    print("-" * 24)
    for proj, (c, r) in results.items():
        display = "Java版" if proj == "MC" else "基岩版"
        c_str = str(c) if c >= 0 else "失败"
        r_str = str(r) if r >= 0 else "失败"
        print(f"{display:<8} {c_str:>8} {r_str:>8}")

    print("\n=== 最新修复的漏洞 (MC) ===")
    for item in recent_mc:
        labels = ", ".join(item.get("labels", [])) if item.get("labels") else "无标签"
        print(f"{item['key']}: {item['summary']} ({item['status']}) [标签: {labels}]")
    print("\n=== 最新修复的漏洞 (MCPE) ===")
    for item in recent_mcpe:
        labels = ", ".join(item.get("labels", [])) if item.get("labels") else "无标签"
        print(f"{item['key']}: {item['summary']} ({item['status']}) [标签: {labels}]")

    xaml_content = generate_xaml(results, recent_mc, recent_mcpe, now)
    filename = "MCBugStats.xaml"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(xaml_content)
    print(f"\n已生成 XAML 文件: {filename} (位于 {os.getcwd()})")
    print("使用说明：将此文件的内容替换到 PCL 主页自定义文件中即可。")

if __name__ == "__main__":
    main()
