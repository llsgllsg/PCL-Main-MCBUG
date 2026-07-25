<StackPanel xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:local="clr-namespace:PCL;assembly=Plain Craft Launcher 2">

    <local:MyHint 
        Text="数据来自 Mojira Public API&#x0a;统计时间：2026-07-25 09:49:38 (UTC+8)" 
        Theme="Blue"
        Margin="0,0,0,15"
    />

    <local:MyCard Title="过去24小时新增与修复漏洞统计" Margin="0,0,0,15" CanSwap="True" IsSwapped="False">
        <StackPanel Margin="25,40,23,15">
            <WrapPanel>
                <GroupBox Header="JAVA 新增" Content="30" />
                <GroupBox Header="JAVA 修复" Content="29" />
                <GroupBox Header="基岩版 新增" Content="27" />
                <GroupBox Header="基岩版 修复" Content="16" />

            </WrapPanel>
            <TextBlock TextWrapping="Wrap" Margin="0,15,0,0" FontSize="11" Foreground="{DynamicResource ColorBrush5}"
                       Text="点我刷新" />
        </StackPanel>
    </local:MyCard>

    <local:MyCard Title="最新提交的Java版漏洞" Margin="0,0,0,15" CanSwap="True" IsSwapped="True">
        <StackPanel Margin="25,15,23,15">
            <local:MyHint Text="点击下方卡片内的按钮可查看详细" Theme="Blue" Margin="0,0,0,10" />
            <WrapPanel>

                <GroupBox Header="MC-310438 - Player can mine the block underneath a Cushion while sitting on it (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310438" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310437 - Game crash upon joining (or) black screen if loading screen suceed (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310437" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310436 - Player Caused Explosions Fail To Pass Attribution While Player Is Dead (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310436" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310435 - Wither asymmetry (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310435" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310434 - Game crashes upon startup (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310434" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310433 - lost access to java but still own bedrock (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310433" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310432 - ClientDisconnection-140 (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310432" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310430 - discs in the inventory (Resolved)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310430" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310429 - Setblock breaks datapack actions and experience if piston triggered (Resolved)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310429" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310428 - can't play multi (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MC-310428" />
                    </StackPanel>
                </GroupBox>

            </WrapPanel>
            <!-- 嵌套子卡片，显示镜像源 -->
            <local:MyCard Title="（镜像源）" Margin="0,15,0,0" CanSwap="True" IsSwapped="True">
                <StackPanel>
                    <WrapPanel>

                <GroupBox Header="MC-310438 - Player can mine the block underneath a Cushion while sitting on it (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310438" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310437 - Game crash upon joining (or) black screen if loading screen suceed (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310437" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310436 - Player Caused Explosions Fail To Pass Attribution While Player Is Dead (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310436" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310435 - Wither asymmetry (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310435" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310434 - Game crashes upon startup (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310434" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310433 - lost access to java but still own bedrock (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310433" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310432 - ClientDisconnection-140 (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310432" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310430 - discs in the inventory (Resolved)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310430" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310429 - Setblock breaks datapack actions and experience if piston triggered (Resolved)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310429" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MC-310428 - can't play multi (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MC-310428" />
                    </StackPanel>
                </GroupBox>

                    </WrapPanel>
                </StackPanel>
            </local:MyCard>
        </StackPanel>
    </local:MyCard>

    <local:MyCard Title="最新提交的寄样板漏洞" Margin="0,0,0,15" CanSwap="True" IsSwapped="True">
        <StackPanel Margin="25,15,23,15">
            <local:MyHint Text="点击下方卡片内的按钮可查看详细" Theme="Blue" Margin="0,0,0,10" />
            <WrapPanel>

                <GroupBox Header="MCPE-241002 - Throwing me out of realm (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-241002" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-241001 - Global Resources Reset Resources Failed to Load Previously error on ipad (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-241001" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-241000 - Inventory snap (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-241000" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240999 - Saving my world is impossible. (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-240999" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240998 - Being kicked off of Realms (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-240998" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240997 - Particle Brightness Depends on Camera Angle (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-240997" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240996 - Banner Phasing Into Floor (Resolved)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-240996" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240995 - The coefficient reversal of instant heath and instant damage effects on undead (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-240995" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240994 - Editing one Dressing Room character slot modifies a different custom skin slot (Bedrock v26.33) (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-240994" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240993 - Wool double slabs have incorrect opacity (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://bugs.mojang.com/browse/MCPE-240993" />
                    </StackPanel>
                </GroupBox>

            </WrapPanel>
            <!-- 嵌套子卡片，显示镜像源 -->
            <local:MyCard Title="（镜像源）" Margin="0,15,0,0" CanSwap="True" IsSwapped="True">
                <StackPanel>
                    <WrapPanel>

                <GroupBox Header="MCPE-241002 - Throwing me out of realm (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-241002" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-241001 - Global Resources Reset Resources Failed to Load Previously error on ipad (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-241001" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-241000 - Inventory snap (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-241000" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240999 - Saving my world is impossible. (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-240999" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240998 - Being kicked off of Realms (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-240998" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240997 - Particle Brightness Depends on Camera Angle (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-240997" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240996 - Banner Phasing Into Floor (Resolved)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-240996" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240995 - The coefficient reversal of instant heath and instant damage effects on undead (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-240995" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240994 - Editing one Dressing Room character slot modifies a different custom skin slot (Bedrock v26.33) (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-240994" />
                    </StackPanel>
                </GroupBox>

                <GroupBox Header="MCPE-240993 - Wool double slabs have incorrect opacity (Open)" Margin="5" MinWidth="200" MinHeight="40">
                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
                        <local:MyButton Width="80" Height="25" ColorType="Highlight" Text="打开" EventType="打开网页" EventData="https://mojira.dev/browse/MCPE-240993" />
                    </StackPanel>
                </GroupBox>

                    </WrapPanel>
                </StackPanel>
            </local:MyCard>
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
                Logo="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.205 11.387.6.113.82-.26.82-.583 0-.288-.01-1.05-.015-2.06-3.338.726-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.468-2.381 1.236-3.221-.124-.3-.536-1.52.117-3.162 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.642.242 2.862.118 3.162.768.84 1.233 1.911 1.233 3.221 0 4.605-2.803 5.62-5.476 5.92.43.37.824 1.102.824 2.222 0 1.606-.015 2.898-.015 3.293 0 .322.216.698.83.578 4.765-1.588 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
                LogoScale="1.1"
                Theme="Color"
                EventType="打开网页"
                EventData="https://github.com/llsgllsg/PCL-Main-MCBUG"
                ToolTip="查看本项目的 GitHub 仓库"
                Margin="20,0,0,10"
            />
        </StackPanel>
    </local:MyCard>

</StackPanel>
