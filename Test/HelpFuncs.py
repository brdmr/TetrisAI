import sys
# Pretty print world
def ppWorld(world):
    for j in world:
        for a in j:
            if a == 0:
                sys.stdout.write(u'\u25A1')
            else:
                sys.stdout.write(u'\u25A0')
        print ""
    print ""

