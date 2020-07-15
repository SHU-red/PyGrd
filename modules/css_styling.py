# Import Gdk
from gi.repository import Gdk, Gtk

def load_css():

    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path("modules/css_styling.css") # TODO styling in css document not working. Only with * definition
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)