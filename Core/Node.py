# This file should contain the node used for the TD-Algorithm

# Basic layout
# * Current world state
# * Current block
# * Neighbours
# * Shrunken world state
class Node:
    world = [[0 for x in range(20)] for x in range(10)]
    block = None
#    neighbours = None
    smallworld = None # Might be better to have a function for this
