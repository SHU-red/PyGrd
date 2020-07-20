#!/bin/bash

sudo pyinstaller PyGrd.py --clean -y --onedir --name PyGrd -i '/icons/PyGrd_96.ico' --add-data 'config.txt:.' --add-data 'modules/setting.ini:modules' --add-data 'icons:icons' --add-data 'modules/css_styling.css:modules' --log-level DEBUG > out.txt
