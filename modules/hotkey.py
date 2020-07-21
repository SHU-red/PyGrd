# Load Hotkey listener
from pynput import keyboard

# Load Grid functions
from modules.grid_functions import *

# Set Hotkeys
hotkey_grid = [
    {keyboard.Key.ctrl, keyboard.Key.alt}
]
hotkey_num = [
    {keyboard.KeyCode(char='0')},
    {keyboard.KeyCode(char='1')},
    {keyboard.KeyCode(char='2')},
    {keyboard.KeyCode(char='3')},
    {keyboard.KeyCode(char='4')},
    {keyboard.KeyCode(char='5')},
    {keyboard.KeyCode(char='6')},
    {keyboard.KeyCode(char='7')},
    {keyboard.KeyCode(char='8')},
    {keyboard.KeyCode(char='9')}
]

# The currently active modifiers
current_grid = set()

# Declare global hotkey indicator
hkey_active = 0

# If key is pressed
def on_press(key):

    # Declare hotkey-indicator as global variable
    global hkey_active

    # Print pushed key for debugging
    print(key)

    # 5 on numpad returns KeyCode <65437>
    if key==keyboard.KeyCode(65437):

        # Has to be replaced by char for extracting the number
        key = keyboard.KeyCode(char='5')

    # If Num-Key detected
    # Has to be placed before Hotkey detection to make sure hotkey has to be pressed first
    if any([key in COMBO for COMBO in hotkey_num]) and hkey_active == 1:

            # Move Active Window to desired grid-field
            move_to_num(key)

            # Kill Grid afterwards
            kill_grid()

    # If Single-Key detected
    if any([key in COMBO for COMBO in hotkey_grid]):

        # Add to Key-List
        current_grid.add(key)

        # If Grid-HotKey detected
        if any(all(k in current_grid for k in COMBO) for COMBO in hotkey_grid):

            # Show configured Grid
            show_grid()

            # Store information that hotkey is pressed
            hkey_active = 1

# If some key is released
def on_release(key):

    # Set indicator to global variable
    global hkey_active

    # Remove from Grid-List
    if any([key in COMBO for COMBO in hotkey_grid]):

        # Try because sometimes number already removed
        try:

            # Delete released button
            current_grid.remove(key)

        # Or do this
        except:

            # Do nothing
            pass

        # Kill grid
        kill_grid()

        # Reset indicator
        hkey_active = 0


# Declare Keyboard listener
listener = keyboard.Listener(on_press=on_press,on_release=on_release)

# Start keyboard Listener
listener.start()