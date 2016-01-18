# This file contains the functions to run the TD-algorithm (e-greedy?)
# For a tetris game.


# Needed functions:
# * Get Possible States
#   - Get Rotations
#   - Get Possible Placements for each Rotation
# * Choose State from new States
#   - Compute reward and long time gain
# * Check if line removed and update accordingly
# * Update  previous states
# * Check terminate ( might be done in get possible states? )

import numpy as np

class TD:
    prevstates = None
    rewardmap = None

    def __init__(self, prevstates, rmap):
        self.rewardmap = rmap
        self.prevstates = prevstates

    # Main method for a run of the algorithm
    # node is the current node to transition away from
    # eps is the epsilon of the epsilon-greedy TD (probability to chose best state)
    def nextState(self, node, eps=0.2):
        # Get all possible next states
        neighbours = getNeighbours(node.world, node.block)

        # Determine which state is the next one.

# Returns all rotations of a given block and corresponding blockbit
    def rotateBlock(self, block, blockbit):
        rotations = [blockbit] # Given blockbit is always a rotation
        if block == 'O': # There is only one rotation for 0
            return rotations
        elif block in ['I', 'S', 'Z']: # There is two rotations for I
            rotations.append(blockbit.transpose())
        else:
            for i in range(1,4):
                rotations.append(np.rot90(blockbit, i))
        return rotations

    # Input is the current world and the possible blocks (with rotations) possible
    def getWorlds(self, world, blocks):
        worlds = [] # This is the array to return containing new worlds we can transision to.
        for block in blocks: # For each block compute new worlds.
            print block.shape
            block_height = block.shape[0];
            block_width = block.shape[1];
            world_height = world.shape[0];
            world_width = world.shape[1];
            for world_index in range(world_width-block_width+1): # Evaluate a current section of the world for a specific block.
                world_block = world[:,world_index:(world_index+block_width)]
                for r in reversed(range(world_height+1)):
                    added = world_block[r-block_height:r,:] + block;
                    if 2 not in added:
                        # Save away baby.
                        world_copy = world.copy();
                        world_copy[r-block_height:r, world_index:world_index+block_width] =   world_copy[r-block_height:r, world_index:world_index+block_width] + block;
                        worlds.append(world_copy)
                        break
        return worlds




    # Returns all neighbouring nodes to the given Node
    def getNeighbours(self, world, block):
        worlds = []
        blockbit = None

        if block is 'S':
            blockbit = np.array([[0,1,1],[1,1,0]])
        elif block is 'Z':
            blockbit = np.array([[1,1,0],[0,1,1]])
        elif block is 'T':
            blockbit = np.array([[0,1,0],[1,1,1]])
        elif block is 'I':
            blockbit = np.array([[1, 1, 1, 1],[0,0,0,0]]) # Line of padding due to width shape of np.array must be defined
        elif block is 'J':
            blockbit = np.array([[1,0,0],[1,1,1]])
        elif block is 'L':
            blockbit = np.array([[0,0,1],[1,1,1]])
        elif block is 'O':
            blockbit = np.array([[1,1],[1,1]])

        # Get all possible rotations for the given block as blockbits
        rots = self.rotateBlock(block, blockbit)

        # Get the possible new worlds from the given block and rotations
        #worlds = self.getWorlds(world, rots);
        return rots



