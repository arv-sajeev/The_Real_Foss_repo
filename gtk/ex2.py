from gi.repository import Gtk
import sys
class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
        self.set_default_size(200, 100)

class MyLabel(Gtk.Label):
    def __init__(self):
        Gtk.Label.__init__(self)
        self.set_text("Hello GNOME!")

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        label = MyLabel()
        win.add(label)
        win.show_all()
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
