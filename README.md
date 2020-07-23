# PyGrd
<p align="center">
  <img src="icons/PyGrd_96.png"><br>
  <b>PyGrd</b><br>
  <br>
  Tray-application for snapping activated window into customizable grid
</p>
  
<p align="center">
  <b>Windows are moved and resized immediately to configuratable grid-tiles</b><br>
  <img src="documentation/windows.png"><br>
  <br>
  <b>Easy configuration via percentual declaration</b><br>
  <img src="documentation/config.png"><br>
  <br>
  <b>Easy configuration picking via TrayIcon</b><br>
  <img src="documentation/menu.png">
</p>

***
## Development
- Developed & tested on Linux Mint 20 Cinnamon
- Developed & testen on Python 3.8
- Has to be ran as root due to handling of tray-icon
***
## How to run
Only tested on Linux Mint 20 Cinnamon
- Modules are used requiring root (Gtk, Gdk, Tkinter, Xlib, ...)
- To run applications as root without terminal-commands or passwords > systemd-services are used
- For using systemd-services see documentation or tutorials (like [this one](https://forums.linuxmint.com/viewtopic.php?t=275464))

Here's the script i use as pygrd.service:
```
[Unit]
Description=PyGrd

[Service]
User=sebastian
Group=nogroup
Type=simple
WorkingDirectory=/home/usr/PycharmProjects/PyGrd
ExecStart=+/home/usr/PycharmProjects/PyGrd/PyGrd.py
Restart=always
RestartSec=3
Environment=DISPLAY=:0

[Install]
WantedBy=multi-user.target
```
***
## Tasks
- [x] Basically running application
- [x] Reading and checking config-files
- [ ] Showing configured grids by pressing Ctr + Alt
- [x] Moving windows to configured grids by pressing Ctr + Alt + NUMPad
- [ ] Moving windows to configured grids by clicking on grid

- [ ] Styling
- [ ] Documentation
