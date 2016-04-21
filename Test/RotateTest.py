import sys

sys.path.insert(0, '/home/brede/Development/Python/TetrisAI/Core')

import TDfuncs as td
import numpy as np


world = np.zeros([20,10])
x = td.TD(None, None)
world[19,0:4] = [1,1,1,1]
s = np.array([[1,1,0],[0,1,1]])
s = np.array([[1],[1],[1],[1]])
print "Current World"
for i in world:
    print i;

print ""

print "Tetroid to place: 'I'"

rots = x.getNeighbours(world, 'I')
for i in range(len(rots)):
    print rots[i]
    print ""

new_worlds = x.getWorlds(world, [s])
for i in reversed(new_worlds):
    for j in i:
        for a in j:
            if a == 0:
                sys.stdout.write(u'\u2591')
            else:
                sys.stdout.write(u'\u2588')
        print ""
    print ""
