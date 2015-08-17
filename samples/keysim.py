# This file is just to simulate a keypress from the script.
# The script waits 2 seconds before it presses 'shift + a'.
import uinput
import time
'''from evdev import uinput, ecodes as e
import time as t
def main():
    t.sleep(2);
    with uinput.UInput() as ui:
        while(True):
            t.sleep(0.3)
            ui.write(e.EV_KEY, e.KEY_LEFT, 1)
            ui.write(e.EV_KEY, e.KEY_LEFT, 0)
            t.sleep(0.02);
            ui.write(e.EV_KEY, e.KEY_LEFT, 1)
            ui.write(e.EV_KEY, e.KEY_LEFT, 0)
            t.sleep(0.02);
            ui.write(e.EV_KEY, e.KEY_SPACE, 1)
            ui.write(e.EV_KEY, e.KEY_SPACE, 0)
            t.sleep(0.02);
            ui.syn();

'''

def main():
    device = uinput.Device([
        uinput.KEY_SPACE,
        uinput.KEY_LEFT,
        uinput.KEY_UP,
        uinput.KEY_H,
        ])
    time.sleep(2);

    while(True):
        device.emit_click(uinput.KEY_H)
        print "Press H";
        time.sleep(0.5)
# Run main
if __name__ == "__main__": main()
