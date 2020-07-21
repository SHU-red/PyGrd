# Import Gdk
from gi.repository import Gdk, Gtk

def load_css():

    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path("modules/css_styling.css")
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)