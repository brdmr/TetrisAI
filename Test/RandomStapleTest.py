import sys
import random
sys.path.insert(0, '/home/brede/Development/Python/TetrisAI/Core')

import TDfuncs as td
import numpy as np
import HelpFuncs as hf

world = np.zeros([20,10])
algObj = td.TD(None, None)

numTetoids = 1

for _ in range(0, numTetoids):
    blockString = "TILJSZO"
    #rand = random.randint(0,len(blockString)-1)
    rand = 1
    addBlock = blockString[rand]
    rotations = algObj.getNeighbours(world, addBlock)
    print addBlock
    newWorlds = algObj.getWorlds(world, rotations)
    randWorld = random.randint(2,len(newWorlds)-1)
    world = newWorlds[randWorld]
    hf.ppWorld(world)
