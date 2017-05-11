#!/usr/bin/python3.4

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import Download



class App():

    def __init__(self):
        """Create te windows for app with Gtk"""

        self.builder = Gtk.Builder()
        self.builder.add_from_file("windowsDlmp3.glade")
        self.builder.connect_signals(self)

        ####################################################
        #Object main window is get here
        self.window = self.builder.get_object("window1")

        ####################################################
        #Object entry is get here

        self.entry1 = self.builder.get_object("entry1")


        ####################################################

        self.window.show_all()


    def on_buttondownload_clicked(self, widget):
        """Event if the button clicked"""
        try:
            Download.Downloadmp3(self.entry1.get_text())
            Download.Downloadmp3.movefile("Download")
            pass
        except Exception as e:
            raise

    def on_window1_delete_event(self, *args):
        """Event if clicked exit"""
        Gtk.main_quit(*args)


###########################################################
#Main
if __name__ == "__main__":
    App()
    Gtk.main()
