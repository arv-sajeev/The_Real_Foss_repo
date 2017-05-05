
from gi.repository import Gtk
import sys
class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
	self.set_default_size(200,1000)
class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
	lab = Gtk.Label(label="para ra ra ra its the one and only dogg",angle=45)
	win.add(lab)
        win.show_all()
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
