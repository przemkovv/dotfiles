# -*- coding: utf-8 -*-

# import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
                format="⌚ %a %-d %b %X",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load",
                format="☢ {avg1}, {avg5}")

status.register("cpu_usage",
                format="↺ {usage:02}%")

# Shows your CPU temperature, if you have a Intel CPU
#status.register("temp",
                #format="{temp:.0f}°C",)

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#

# Displays whether a DHCP client is running
# status.register("runwatch",
# name="DHCP",
# path="/var/run/dhclient*.pid",)

# Shows the address and up/down state of eth0. If it is up the address is shown
# in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces-py3
status.register("network",
                interface="enp0s25",
                format_up="{v4cidr}",)


# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
                path="/home",
                format="⌂ {used}/{total}G",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
                format="♪{volume}",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
                format="☊ {title}{status}{album}",
                status={
                       "pause": " ▷ ",
                       "play": " ▶ ",
                       "stop": " ◾ ",
                },)

status.run()
