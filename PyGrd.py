#!/usr/bin/python3.8

# Load os module
import os.path

# Load AppIndicator Module
import gi
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

# Import menu filie
from modules.menu import *

# Start hotkey listener
from modules.hotkey import *

def main():

    # Configure Tray icon
    indicator = appindicator.Indicator.new("customtray", os.path.abspath('icons/PyGrd_96.ico'),
                                           appindicator.IndicatorCategory.APPLICATION_STATUS)

    # Activate Tray icon
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

    # Add Menu to Tray icon
    indicator.set_menu(build_menu())

    gtk.main()

# Close Prorgram
def quit(_):
    gtk.main_quit()

def declare_classes():
    class Window_conf:
        def __init__(self, x_ul, y_ul, width, height):
            self.x_ul = x_ul
            self.y_ul = y_ul
            self.width = width
            self.height = height

if __name__ == "__main__":
    main()