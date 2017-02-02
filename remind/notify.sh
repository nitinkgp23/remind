#!/bin/sh
export DISPLAY=:0

notify-send "$1"
aplay -q ~/remind/res/notifications/Mallet.wav
