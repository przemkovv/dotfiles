#!/bin/sh

case $BLOCK_BUTTON in
  2)df -h | grep /dev/sdg1 | awk '{print $3,$2,$5}' ;;
  1)df -h | grep /dev/md127 | awk '{print $3,$2,$5}' ;;

esac

df -h | grep /dev/md127 | awk '{print $3,$2,$5}'
