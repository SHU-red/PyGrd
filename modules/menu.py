# import os functions
import sys

# Import gi from main-package
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

# Import ConfigParser
import configparser

# Import module for dialogs
from modules.dialogs import *

# Import settings module
from modules.setting import *

def build_menu():

    # Create Menu
    menu = gtk.Menu()

    # Write gtk stlye settings
    menu_settings = gtk.Settings.get_default()
    menu_settings.set_property('gtk-application-prefer-dark-theme', True)

    # Show available configs
    reload_menu(menu)

    # Separator
    menu_separator = gtk.SeparatorMenuItem()
    menu.append(menu_separator)

    # Reload ini-file
    exittray = gtk.MenuItem('Reload configs')
    exittray.connect('activate', reload_configs,menu)
    menu.append(exittray)

    # Reload ini-file
    exittray = gtk.MenuItem('Show shortcuts')
    exittray.connect('activate', dlg_shortcuts)
    menu.append(exittray)

    # Separator
    menu_separator = gtk.SeparatorMenuItem()
    menu.append(menu_separator)

    # Exit PyGrd
    exittray = gtk.MenuItem('Exit')
    exittray.connect('activate', quit)
    menu.append(exittray)

    menu.show_all()
    return menu

def reload_menu(menu_item):


    # Load active setting
    setting = load_setting_from_file()

    # Parse from config-file
    config = configparser.ConfigParser()
    config.read('config.ini')



    # Loop over all configs
    for conf in config.sections():
        menu_setting = gtk.MenuItem(conf)
        menu_setting.connect('activate', write_setting_to_file,conf)

        # If no config was stored in setting.ini, use currently loaded setting
        if setting == "":
            setting = conf
            write_setting_to_file("",conf)

        # If detected as currently active configuration
        if conf == setting:

            # Highlight the active setting
            menu_setting.select()

            # Write setting into global arrays
            setting_to_global_arrays(setting, config)

        menu_item.append(menu_setting)

def reload_configs(self,menu):
    os.execl(sys.executable, sys.executable, *sys.argv)

def read_setting(setting):
    print("Reload Setting")