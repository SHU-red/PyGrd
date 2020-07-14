# Import global variables
import modules.glob_vars as g

# Import module for dialogs
# from modules.dialogs import *

# Import Gdk-Module
import gi
gi.require_version('Gdk','3.0')
gi.require_version('Gtk','3.0')
from gi.repository import Gdk, Gtk, GdkX11

def show_grid():

    # If Current setting not valid
    if not g.SValid:
        dlg_setting_not_valid()

    # If current setting valid
    else:

        # Get Screen sizes
        get_screen_size()

        print("Show grid hotkey pressed")

# Move and resize currently active Window to Chosen grid
def move_to_num():

    # If Current setting not valid
    if not g.SValid:
        dlg_setting_not_valid()

    # If current setting valid
    else:

        print("Move to num Hotkey pressed")

# Clean Screen from shown Grid
def kill_grid():
    print ("Kill Grid")

# Get Screen sizes
def get_screen_size():

    # Read monitor properties
    display = Gdk.Display().get_default()

    # For each monitor
    for i in range(display.get_n_monitors()):

        # Get Monitor
        monitor = display.get_monitor(i)

        # Get Area
        w_area = monitor.get_workarea()

        print(w_area.x, w_area.y,
              w_area.width, w_area.height)