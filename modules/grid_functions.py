# Import global variables
import modules.glob_vars as g

# Impmort Tkinter
import tkinter as tk

# Import module for dialogs
from modules.dialogs import *

import Xlib

# Import Gdk-Module
import gi
gi.require_version('Gdk','3.0')
gi.require_version('Gtk','3.0')
from gi.repository import Gdk as gdk, Gtk as gtk, GdkX11

# Show grid
def show_grid():

    # If Current setting not valid
    if not g.SValid:
        dlg_setting_not_valid()

    # If current setting valid
    else:

        # If screensize not read since change
        if not g.Res_Chk:
            # Read screensize
            get_screen_size()

        print("Show grid hotkey pressed")

        # TODO show grid

# Move and resize currently active Window to Chosen grid
def move_to_num(number):

    # If Current setting not valid
    if not g.SValid:
        dlg_setting_not_valid()

    # If current setting valid
    else:

        # If screensize not read since change
        if not g.Res_Chk:
            # Read screensize
            get_screen_size()

        # Convert keycode to integer number
        int_number = ord(format(number.char)) - 48

        print(int_number)

        # Initiate counter
        n = 0

        # Loop to check if window Numerator is defined
        while n < len(g.Numeration):

            # If Numeration equals the pushed button
            if g.Numeration[n] == int_number:

                # Re-Calculate scaling target in pixels
                # (Done as late as possible in case of more loading situations in future)
                scal_x = int(round(g.X_UpLeCorner[n]*0.01*g.X_ScreenSize,0))
                scal_y = int(round(g.Y_UpLeCorner[n]*0.01*g.Y_ScreenSize,0))
                scal_w = int(round(g.X_Width[n]*0.01*g.X_ScreenSize,0))
                scal_h = int(round(g.Y_Height[n]*0.01*g.Y_ScreenSize,0))

                # Move Window
                display = Xlib.display.Display()
                root = display.screen().root
                windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
                window = display.create_resource_object('window', windowID)
                window.configure(x=scal_x,y=scal_y,width=scal_w,height=scal_h)
                display.sync()

                # Exit while loop
                break

            # Increase counter
            n += 1

# Clean Screen from shown Grid
def kill_grid():
    print ("Kill Grid")

    # TODO Kill grid

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

    # Set indicator for checked Screen size
    g.Res_Chk = 1

    # TODO Check if screen resolution changes an reset indicator for checking screen resolution