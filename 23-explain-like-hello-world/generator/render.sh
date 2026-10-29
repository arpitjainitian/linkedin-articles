#!/bin/zsh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --hide-scrollbars --window-size=1920,1080 --screenshot=$PWD/$1.png file://$PWD/$1.html 2>/dev/null
