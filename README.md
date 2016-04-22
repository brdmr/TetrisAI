# Tetris AI
This project aims to create an AI by implementing the reinforcement learning algorithm Q-learning for the Tetris game. The long term goal is to be able to play against the bot over at tetrisfriends.com

## Q-learning
The Q-learning algorithm can be seen as a combination of Dynamic Programming and a Heuristic Search. 
To get a better understanding of Q-learning we will define the functions and
states needed in the general case. Further I will explain the current though
process of how to translate this into the Tetris problem. 

### Core of the Q-learning
The Q-learning
algorithm can be defined as follows. First it needs to define a decision
making _agent_. Then it needs a set of _states_ __S__ that the agent can be in.
Finally we need to define a set of _actions_ __A__ that the agent kan make 
based on its current state to transition into a new state. In the long term the
agent aim to get a maximum reward. Therefore we need to define a 
_value-function_ __Q__ that returns the expected reward based on the current 
state and possible actions.

Therefore to implement the Q-learning algorithm we need to define:
* How the states S looks
* The possible actions given a state
* The value function that given an action returns the rewards for the possible
following states.

There are some more concepts as epsilon-greedy etc. not described in this document, but will be implemented. To get a full overview of the Q-learning algorithm please have a look at [Wikipedia's Q-learning page](https://en.wikipedia.org/wiki/Q-learning)
## The Q-learning algorithm for Tetris
![A tetris game board.](http://www.play.vg/g2_imgs/g2_6.gif)
To use Q-learning for Tetris we need to define the bullet points defined above.
As seen in the image is a possible game state in the tetris game. One possible
way to define the states S for our algorithm would be to just transcode the game
board and the placed bits into a binary sequence where 1 represent a block that
is covered and 0 a block that is not covered by a piece. However this would
result in a very large sate space where many states would look the same in the
sense of good playable moves. Therefore we want to decrease the state space,
this will let our algorithm converge faster as well. What we do is to store the
height of each column in the game. So for example the state in the image would
be [6,4,2,4,3,3,3,0,0,1]. The square to be placed is not part of the current
state but is used in the action function to determine which states we can
transition to. The action function is takes the next tetroid to be places and the current state as parameters and returns a list of all possible states based
based on how we place the tetroid in the current state. Finally we have a value 
function that gets a reward when removing one (or several) lines. It gets a penalty for placing the tetroid in a place that results in a hole in the board as well as in the case of losing the game. 

## Usage
Currently the code is under development and unfortunately no runnable scripts are available.
