# Import os functions
import os, sys

# Set path to settings-file
settings_file = "modules/setting.ini"

# Import global variables
import modules.glob_vars as g

# Import module for dialogs
from modules.dialogs import *

def load_setting_from_file():

    # Make sure that file exists
    check_for_file_and_create()

    # Open file
    file = open(settings_file, 'r')

    setting = file.read()

    file.close()

    return setting


def write_setting_to_file(self, conf):

    # Make sure that file exists
    check_for_file_and_create()

    # Open file
    file = open(settings_file,'w')

    # Write String
    file.write(conf)

    # Close file
    file.close()

    # Restart Program
    os.execl(sys.executable, sys.executable, *sys.argv)

    return

# Check if storage-file exists and create if needed
def check_for_file_and_create():

    # Check if file does not exist
    if not os.path.isfile(settings_file):

        # Create file
        os.mknod(settings_file)

def setting_to_global_arrays(setting_name, read_config):

    # Reading config-strings and convert to int-arrays
    g.SName = setting_name
    g.Numeration = list(map(int,read_config[setting_name]['Numeration'].split(',')))
    g.SLength = len(g.Numeration)
    g.X_UpLeCorner = list(map(int,read_config[setting_name]['X_UpLeCorner'].split(',')))
    g.Y_UpLeCorner = list(map(int,read_config[setting_name]['Y_UpLeCorner'].split(',')))
    g.X_Width = list(map(int,read_config[setting_name]['X_Width'].split(',')))
    g.Y_Height = list(map(int,read_config[setting_name]['Y_Height'].split(',')))

    # Checking string length
    length_equal = g.SLength == len(g.X_UpLeCorner) == len(g.Y_UpLeCorner) == len(g.X_Width) == len(g.Y_Height)

    # If Arrays have same length
    if length_equal:

        # Add-up for each direction
        add_X = list(map(lambda x, y: x + y, g.X_UpLeCorner , g.X_Width))
        add_Y = list(map(lambda x, y: x + y, g.Y_UpLeCorner, g.Y_Height))

        # Checking value range
        sizes_merged = g.X_Width + g.Y_Height + add_X + add_Y
        coord_merges = g.X_UpLeCorner + g.Y_UpLeCorner
        range_OK = max(sizes_merged) <= 100 and min(sizes_merged) > 0 and max(coord_merges) <= 100 and min(coord_merges) >= 0 and min(g.Numeration) >= 0 and max(g.Numeration) <= 9

    else:
        range_OK = False

    # All checks have to be TRUE
    g.SValid = length_equal and range_OK

    # If config is not valid
    if not g.SValid:

        # Show message to user that config is not valid
        dlg_setting_not_valid()