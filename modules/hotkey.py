# Load Hotkey listener
from pynput import keyboard

# Load Grid functions
from modules.grid_functions import *

# Set Hotkeys
hotkey_grid = [
    {keyboard.Key.ctrl, keyboard.Key.alt}
]
hotkey_num = [
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='0')},
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='1')},
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='2')},
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='3')},
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='4')},
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='5')}, #TODO Numpad 5 is not interpreted as char --> Different comparison
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='6')},
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='7')},
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='8')},
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='9')}
]

# The currently active modifiers
current_grid = set()
current_num = set()

def on_press(key):

    # If Single-Key detected
    if any([key in COMBO for COMBO in hotkey_grid]):

        # Add to Key-List
        current_grid.add(key)

        # If Grid-HotKey detected
        if any(all(k in current_grid for k in COMBO) for COMBO in hotkey_grid):

            # Show configured Grid
            show_grid()

    # If Num-Key detected
    if any([key in COMBO for COMBO in hotkey_num]):

        # Add to Key-List
        current_num.add(key)

        # If Num-Hotkey detected
        if any(all(k in current_num for k in COMBO) for COMBO in hotkey_num):

            # Move Active Window to desired grid-field
            move_to_num(key)

            # Kill Grid afterwards
            kill_grid()

def on_release(key):

    # Remove from Grid-List
    if any([key in COMBO for COMBO in hotkey_grid]):
        current_grid.remove(key)
        kill_grid()


    # Remove from Num-List
    if any([key in COMBO for COMBO in hotkey_num]):
        current_num.remove(key)

# Declare Keyboard listener
listener = keyboard.Listener(on_press=on_press,on_release=on_release)

# Start keyboard Listener
listener.start()