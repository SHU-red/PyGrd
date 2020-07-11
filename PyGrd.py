#!/usr/bin/python

# Load os module
import os

# Load AppIndicator Module
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

# Load configparser
import configparser

# Load Configuration Module
import load_config

# Declare classes
load_config.declare_classes()

# Load configuration
load_config.reload_config()

# Get screen resolution
Screen_width = gtk.gdk.screen_width()
Screen_height = gtk.gdk.screen_height()

def main():
    indicator = appindicator.Indicator.new("customtray", "PyGrd.png",
                                           appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())
    gtk.main()


def menu():
    menu = gtk.Menu()

    command_one = gtk.MenuItem('My Notes')
    command_one.connect('activate', note)
    menu.append(command_one)
    exittray = gtk.MenuItem('Exit Tray')
    exittray.connect('activate', quit)
    menu.append(exittray)

    menu.show_all()
    return menu


def note(_):
    os.system("gedit $HOME/Documents/notes.txt")


def quit(_):
    gtk.main_quit()

def load_config():



if __name__ == "__main__":
    main()