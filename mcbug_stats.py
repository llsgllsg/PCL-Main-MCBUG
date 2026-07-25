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

def get_recent_issues(project: str, limit=10, max_retries=3):
    """
    获取指定项目最新提交的漏洞（按创建时间倒序），不限状态。
    """
    url = "https://bugs.mojang.com/api/jql-search-post"
    # 按 created 降序，不限制状态
    jql = "ORDER BY created DESC"
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
                    created = fields.get("created", "")
                    result.append({
                        "key": key,
                        "summary": summary,
                        "status": status,
                        "created": created
                    })
                # 按创建时间降序排序（API 本身已经排序，但为保险再排一次）
                if result and result[0]["created"]:
                    result.sort(key=lambda x: x["created"], reverse=True)
                return result
            else:
                return []
        except Exception as e:
            print(f"请求失败 (尝试 {attempt+1}/{max_retries}): {e}")
            time.sleep(2)
    return []

def generate_xaml(results, recent_mc, recent_mcpe, timestamp):
    display_names = {
        "MC": "JAVA",
        "MCPE": "基岩版"
    }
    groupboxes = ""
    for proj, (created, resolved) in results.items():
        c_str = str(created) if created >= 0 else "失败"
        r_str = str(resolved) if resolved >= 0 else "失败"
        display_name = display_names.get(proj, proj)
        groupboxes += f'                <GroupBox Header="{display_name} 新增" Content="{c_str}" />\n'
        groupboxes += f'                <GroupBox Header="{display_name} 修复" Content="{r_str}" />\n'

    def build_vulnerability_cards(items, version_name):
        if not items:
            return f'    <local:MyCard Title="{version_name} - 暂无数据" Margin="0,0,0,10" CanSwap="True" IsSwapped="False">\n        <StackPanel Margin="25,20,23,20"><TextBlock Text="暂未获取到数据" /></StackPanel>\n    </local:MyCard>\n'
        cards = ""
        for item in items:
            key = item["key"]
            safe_summary = item["summary"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            status = item.get("status", "未知")
            cards += f'''
    <local:MyCard Title="{key} - {safe_summary} ({status})" Margin="0,0,0,10" CanSwap="True" IsSwapped="False">
        <StackPanel Margin="25,20,23,20" HorizontalAlignment="Center" Orientation="Horizontal">
            <local:MyButton Margin="0,0,10,0" Width="120" Height="30" ColorType="Highlight" Text="官方源" EventType="打开网页" EventData="https://bugs.mojang.com/browse/{key}" />
            <local:MyButton Width="120" Height="30" Text="镜像源" EventType="打开网页" EventData="https://mojira.dev/browse/{key}" />
        </StackPanel>
    </local:MyCard>
'''
        return cards

    mc_cards = build_vulnerability_cards(recent_mc, "Java版")
    mcpe_cards = build_vulnerability_cards(recent_mcpe, "基岩版")

    github_logo = "M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.205 11.387.6.113.82-.26.82-.583 0-.288-.01-1.05-.015-2.06-3.338.726-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.468-2.381 1.236-3.221-.124-.3-.536-1.52.117-3.162 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.642.242 2.862.118 3.162.768.84 1.233 1.911 1.233 3.221 0 4.605-2.803 5.62-5.476 5.92.43.37.824 1.102.824 2.222 0 1.606-.015 2.898-.015 3.293 0 .322.216.698.83.578 4.765-1.588 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"

    xaml = f'''<StackPanel xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:local="clr-namespace:PCL;assembly=Plain Craft Launcher 2">

    <local:MyHint 
        Text="数据来自 Mojira Public API&#x0a;统计时间：{timestamp} (UTC+8)" 
        Theme="Blue"
        Margin="0,0,0,15"
    />

    <local:MyCard Title="过去24小时新增与修复漏洞统计" Margin="0,0,0,15" CanSwap="True" IsSwapped="False">
        <StackPanel Margin="25,40,23,15">
            <WrapPanel>
{groupboxes}
            </WrapPanel>
            <TextBlock TextWrapping="Wrap" Margin="0,15,0,0" FontSize="11" Foreground="{{DynamicResource ColorBrush5}}"
                       Text="点我刷新" />
        </StackPanel>
    </local:MyCard>

    <local:MyCard Title="最新提交的Java版漏洞" Margin="0,0,0,15" CanSwap="True" IsSwapped="True">
        <StackPanel Margin="25,15,23,15">
            <local:MyHint Text="点击下方卡片内的按钮可查看详细" Theme="Blue" Margin="0,0,0,10" />
            {mc_cards}
        </StackPanel>
    </local:MyCard>

    <local:MyCard Title="最新提交的基岩版漏洞" Margin="0,0,0,15" CanSwap="True" IsSwapped="True">
        <StackPanel Margin="25,15,23,15">
            <local:MyHint Text="点击下方卡片内的按钮可查看详细" Theme="Blue" Margin="0,0,0,10" />
            {mcpe_cards}
        </StackPanel>
    </local:MyCard>

    <local:MyCard Title="操作" Margin="0,0,0,15" CanSwap="False">
        <StackPanel Margin="25,20,23,20" HorizontalAlignment="Center" Orientation="Horizontal">
            <local:MyIconButton 
                Width="180" 
                Height="35" 
                Padding="15,0,15,0"
                Logo="M511.376609 1023.999739a494.479955 494.479955 0 1 1 424.923283-747.341996 31.37895 31.37895 0 1 1-54.128689 32.163424 431.460564 431.460564 0 1 0 60.66597 220.698616v-32.424915a31.37895 31.37895 0 0 1 62.7579-4.706843c0 12.290089 1.568948 24.580178 1.568948 37.131758 0 273.448865-221.827354 495.264429-495.787412 494.479956z M911.458223 325.295116h-259.660812a31.37895 31.37895 0 0 1 0-62.7579H879.817782V31.37895a31.640441 31.640441 0 0 1 63.019391 0v261.491251a31.640441 31.640441 0 0 1-31.37895 32.424915"
                LogoScale="0.8"
                Theme="Color"
                EventType="刷新主页"
                ToolTip="数据存在部分延迟"
                Margin="0,0,20,10"
            />
            <local:MyIconButton 
                Width="180"
                Height="35"
                Padding="15,0,15,0"
                Logo="{github_logo}"
                LogoScale="1.1"
                Theme="Color"
                EventType="打开网页"
                EventData="https://github.com/llsgllsg/PCL-Main-MCBUG"
                ToolTip="查看本项目的 GitHub 仓库"
                Margin="20,0,0,10"
            />
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

    print("\n(MC)...")
    recent_mc = get_recent_issues("MC", limit=10)
    print("(MCPE)...")
    recent_mcpe = get_recent_issues("MCPE", limit=10)

    print("\n24")
    print(f"{'项目':<8} {'新增':>8} {'修复':>8}")
    print("-" * 24)
    display_names = {"MC": "JAVA", "MCPE": "基岩版"}
    for proj, (c, r) in results.items():
        c_str = str(c) if c >= 0 else "失败"
        r_str = str(r) if r >= 0 else "失败"
        display = display_names.get(proj, proj)
        print(f"{display:<8} {c_str:>8} {r_str:>8}")

    print("\nJAVA")
    for item in recent_mc:
        print(f"{item['key']}: {item['summary']} ({item['status']})")
    print("\n基岩版")
    for item in recent_mcpe:
        print(f"{item['key']}: {item['summary']} ({item['status']})")

    xaml_content = generate_xaml(results, recent_mc, recent_mcpe, now)
    filename = "MCBugStats.xaml"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(xaml_content)
    print(f"\n成功: {filename} (位于 {os.getcwd()})")

if __name__ == "__main__":
    main()
