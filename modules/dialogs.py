# Import gi from main-package
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

# Import global variables
import modules.glob_vars as g

def dlg_shortcuts(self):

    # Do nothing
    pass

def dlg_setting_not_valid():

    # Show info that Message is not valid
    msgBox = gtk.MessageDialog(text = 'Configuration error!',
                               buttons = gtk.ButtonsType.OK,
                               type = gtk.MessageType.ERROR,
                               secondary_text='The configured values of\n\n'
                                              '[' + g.SName + ']\n\n'
                                              'in\n\n'
                                              'config.ini\n\n'
                                              'are faulty!\n\n'
                                              'Please make sure that:\n'
                                              '- Numeration has values from 1-9\n'
                                              '- Sizes and Positions are in % from 0-100\n'
                                              '- Sizes and Positions are added in X- and Y-direction not exceeding 0-100\n'
                                              '- Array-Sizes match\n\n'
                                              'Grid-functions will be suspended until the config-file is fixed!')
    # Run Dialog
    msgBox.run()

    # Close after Button was pushed
    msgBox.destroy()