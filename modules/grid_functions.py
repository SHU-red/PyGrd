# Import global variables
import modules.glob_vars as g

# Impmort Tkinter
import tkinter as tk

# Import module for dialogs
# from modules.dialogs import *

import Xlib

# Import Gdk-Module
import gi
gi.require_version('Gdk','3.0')
gi.require_version('Gtk','3.0')
from gi.repository import Gdk as gdk, Gtk as gtk, GdkX11

def show_grid():

    # If Current setting not valid
    if not g.SValid:
        dlg_setting_not_valid()

    # If current setting valid
    else:

        print("Show grid hotkey pressed")

# Move and resize currently active Window to Chosen grid
def move_to_num():

    # If Current setting not valid
    if not g.SValid:
        dlg_setting_not_valid()

    # If current setting valid
    else:

        display = Xlib.display.Display()
        root = display.screen().root
        windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
        window = display.create_resource_object('window', windowID)
        window.configure(x = 20, y = 20, width=200, height=200)
        display.sync()

        print("Move to num Hotkey pressed")

        # screen = gtk.gdk.screen_get_default()
        # active_window = screen.get_active_window()
        #active_window.move(20,20)
        # active_window = gtk.Application.get_active_window()
        # active_window = gtk.App
        #
        #
        # gtk.move(active_window,200,200)

# Clean Screen from shown Grid
def kill_grid():
    print ("Kill Grid")

# Get Screen sizes
def get_screen_size():

    # Create a dummy tkinter window
    root = tk.Tk()

    # Set to maximize for getting the ratios and transparent to not interrupt user
    root.attributes('-zoomed',True)

    # Generate window
    root.update()

    # read size of usable space
    g.X_ScreenSize = root.winfo_width()
    g.Y_ScreenSize = root.winfo_height()

    # immediately destroy window
    root.destroy()