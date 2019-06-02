#!/bin/sh
#~/scripts/i3blocks/blocklets/date.sh

case $BLOCK_BUTTON in
  1)gsimplecal ;;
  2)galculator ;;

esac

date '+%a, %d %b %Y, %H:%M'
