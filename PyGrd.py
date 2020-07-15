#!/usr/bin/python

# Load os module
import os

# Load AppIndicator Module
import gi
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

# Import menu filie
from modules.menu import *

# Start hotkey listener
from modules import hotkey

# Import Screen-size module
from modules.grid_functions import get_screen_size

def main():

    # Read screensize
    get_screen_size()

    # Configure Tray icon
    indicator = appindicator.Indicator.new("customtray", os.path.abspath('PyGrd.png'),
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




def activate_setting(setting):

    # Dummy
    Test = 3




if __name__ == "__main__":
    main()