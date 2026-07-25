import requests
import time
from datetime import datetime
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

def generate_xaml(results, timestamp):
    groupboxes = ""
    for proj, (created, resolved) in results.items():
        c_str = str(created) if created >= 0 else "失败"
        r_str = str(resolved) if resolved >= 0 else "失败"
        groupboxes += f'                <GroupBox Header="{proj} 新增" Content="{c_str}" />\n'
        groupboxes += f'                <GroupBox Header="{proj} 修复" Content="{r_str}" />\n'

    xaml = f'''<StackPanel xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:local="clr-namespace:PCL;assembly=Plain Craft Launcher 2">

    <local:MyHint 
        Text="📊 数据来自 Mojira Public API&#x0a;统计时间：{timestamp}" 
        Theme="Blue"
        Margin="0,0,0,15"
    />

    <local:MyCard Title="📈 过去24小时新增与修复漏洞统计" Margin="0,0,0,15" CanSwap="True" IsSwapped="False">
        <StackPanel Margin="25,40,23,15">
            <WrapPanel>
{groupboxes}
            </WrapPanel>
            <TextBlock TextWrapping="Wrap" Margin="0,15,0,0" FontSize="11" Foreground="{{DynamicResource ColorBrush5}}"
                       Text="每小时自动更新。由于 API 缓存原因，数据可能有 5-30 分钟的延迟。" />
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
                ToolTip="手动刷新数据"
                Margin="0,0,20,10"
            />
            <local:MyIconButton 
                Width="180"
                Height="35"
                Padding="15,0,15,0"
                Logo="M512 64c81.636 0 156.8 19.911 225.493 59.733s122.951 94.08 162.773 162.773S960 430.364 960 512s-19.911 156.8-59.733 225.493-94.08 122.951-162.773 162.773S593.636 960 512 960s-156.8-19.911-225.493-59.733-122.951-94.08-162.773-162.773S64 593.636 64 512s19.911-156.8 59.733-225.493 94.08-122.951 162.773-162.773S430.364 64 512 64z m119.467 812.373c57.742-17.92 108.516-48.782 152.32-92.587 43.804-43.805 75.164-94.578 94.08-152.32 18.916-57.742 23.396-117.476 13.44-179.2-9.956-61.724-32.853-117.476-68.693-167.253-35.84-49.778-81.138-88.604-135.893-116.48C631.964 140.658 573.724 126.72 512 126.72s-119.964 13.938-174.72 41.813-100.053 66.702-135.893 116.48-58.738 105.529-68.693 167.253c-9.956 61.724-5.476 121.458 13.44 179.2s50.276 108.516 94.08 152.32c43.804 43.804 94.578 74.667 152.32 92.587h2.987c5.973 0 10.951-1.493 14.933-4.48 3.982-2.987 5.973-7.467 5.973-13.44v-65.707l-20.907 2.987H377.6c-19.911 1.991-38.329-1.991-55.253-11.947S293.974 759.893 288 741.973l-17.92-32.853-11.947-11.947-23.893-17.92c-3.982-3.982-5.973-6.969-5.973-8.96s0.996-3.982 2.987-5.973l14.933-2.987c5.973 0 11.947 1.493 17.92 4.48 5.973 2.987 11.947 5.476 17.92 7.467l11.947 14.933 11.947 11.947c7.964 13.938 17.422 24.889 28.373 32.853 10.951 7.964 23.893 11.449 38.827 10.453 14.933-0.996 29.369-4.48 43.307-10.453 1.991-9.956 4.978-19.413 8.96-28.373 3.982-8.96 8.96-16.427 14.933-22.4-25.884-1.991-49.778-7.467-71.68-16.427-21.902-8.96-40.818-21.404-56.747-37.333-15.929-15.929-26.88-34.844-32.853-56.747-7.964-25.884-11.947-52.764-11.947-80.64 0-17.92 3.484-35.84 10.453-53.76 6.969-17.92 16.427-33.849 28.373-47.787-1.991-7.964-3.484-15.431-4.48-22.4s-1.493-14.933-1.493-23.893 0.996-17.92 2.987-26.88c1.991-8.96 3.982-18.418 5.973-28.373h8.96c7.964 0 16.427 0.996 25.387 2.987s17.422 4.978 25.387 8.96l26.88 14.933 20.907 11.947c63.716-17.92 127.431-17.92 191.147 0l20.907-11.947 26.88-14.933c7.964-3.982 15.929-6.969 23.893-8.96 7.964-1.991 16.924-2.987 26.88-2.987h5.973c3.982 9.956 6.969 19.413 8.96 28.373 1.991 8.96 2.987 17.92 2.987 26.88 0 8.96-0.498 16.924-1.493 23.893s-2.489 14.436-4.48 22.4c11.947 13.938 21.404 29.867 28.373 47.787 6.969 17.92 10.453 35.84 10.453 53.76 0 27.876-3.982 54.756-11.947 80.64-5.973 21.902-16.924 40.818-32.853 56.747-15.929 15.929-35.342 28.373-58.24 37.333-22.898 8.96-47.289 14.436-73.173 16.427 9.956 7.964 16.924 18.418 20.907 31.36 3.982 12.942 5.973 26.382 5.973 40.32v104.533c0 5.973 1.991 10.453 5.973 13.44 3.982 2.987 7.964 4.48 11.947 4.48h5.972z"
                LogoScale="1"
                Theme="Color"
                EventType="打开网页"
                EventData="https://bugs.mojang.com/"
                ToolTip="访问 Mojira 官方漏洞追踪器"
                Margin="20,0,0,10"
            />
        </StackPanel>
    </local:MyCard>

</StackPanel>'''
    return xaml

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"统计时间: {now}\n")

    projects = ["MC", "MCPE"]
    results = {}
    for proj in projects:
        print(f"正在统计 {proj} 项目...")
        created = get_issue_count("created >= -24h", project=proj)
        resolved = get_issue_count("resolutiondate >= -24h", project=proj)
        results[proj] = (created, resolved)

    print("\n=== 过去24小时统计 ===")
    print(f"{'项目':<8} {'新增':>8} {'修复':>8}")
    print("-" * 24)
    for proj, (c, r) in results.items():
        c_str = str(c) if c >= 0 else "失败"
        r_str = str(r) if r >= 0 else "失败"
        print(f"{proj:<8} {c_str:>8} {r_str:>8}")

    xaml_content = generate_xaml(results, now)
    with open("MCBugStats.xaml", "w", encoding="utf-8") as f:
        f.write(xaml_content)
    print("\n成功生成 MCBugStats.xaml")

if __name__ == "__main__":
    main()
