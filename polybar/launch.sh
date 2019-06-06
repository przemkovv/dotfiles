#!/bin/bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar, using default config location ~/.config/polybar/config
if [ "$HOSTNAME" = "legolas" ]; then
  polybar legolas &
elif [ "$HOSTNAME" = "gandalf" ]; then
  polybar gandalf_dvi1 &
  polybar gandalf_dp0 &
  polybar gandalf_hdmi0 &
else
  polybar legolas &
fi

echo "Polybar launched..."
