from gi.repository import Gtk
import sys

class MyWindow(Gtk.Window):
	def _init_(self,app):
		Gtk.Window._init(self,title="heh heh",application=app)
		l1 = Gtk.Label(label="hello",angle=45)
		l2 = Gtk.Label(label="you Blithering",angle=45)
		l3 = Gtk.Label(label="idiot",angle=45)
		
		grid = Gtk.grid()
		grid.attach(l1)
		grid.attach(l2)
		grid.attach(l3)
		self.add(grid)

class MyApplication(Gtk.Application):
	def _init_(self):
		Gtk.Application._init(self)

	def do_activate(self):
		win = MyWindow(self)
		win.show_all
app = MyApplication()
exit_status=app.run(sys.argv)
sys.exit(exit_status)
