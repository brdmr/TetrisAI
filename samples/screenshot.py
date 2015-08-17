# This script takes a screenschot from the desktop 10 seconds after launch.
import gtk.gdk
import time as t
for i in range(10):
    t.sleep(5)
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, sz[0], sz[1]);
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0], sz[1])

    if ( pb != None):
      name = "pics/screenshot" + str(i) + ".png"
      pb.save(name,"png")
      print "Screenshot saved to screenshot.png."
    else:
      print "Unable to get the screenshot."
