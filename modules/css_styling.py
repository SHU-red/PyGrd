import gi
gi.require_version("Gtk", "3.0")

# Import Gdk
from gi.repository import Gdk, Gtk

# Import OS
import os

def load_css():

    # Generated absolute path for working load_from_path command
    css_file = os.path.abspath("modules/css_styling.css")

    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path(css_file)
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)