"""
    This script is a TD-learning shell
    containing of two functions
    * init
    * run

    The init function is used to setup the learning algorithm
    The run function is used to run the learning algorithm

"""

class Qlearn:

    def __init__(self, q_table, q_f, action_f, policy_f, reward_f, def_val):
        """
        This is the init function which is just a setup function for the
        necessary functions used to run the Q-learning algorithm.

            Args:
                    * q_table is a (key, value) table that given a state returns
                      a reward, if the key is not present in the map, the key is
                      inserted with valued def_val

                    * q_f is a function that given a state and an action returns
                      the resulting state of the given action on the given state.

                    * action_f is a function that given a state s returns a list
                      of all possible actions to take.

                    * policy_f is a function that given a list of (actions, rewards)
                      selects an action based on the policy determined in
                      the function

                    * reward_f is a function that given a state returns it's
                      immediate reward.

                    * def_val is a variable that acts as the default reward
                      of an unknown key (state) in the q_map

            Returns: Nothing
        """
        self.q_table = q_table
        self.q_f = q_f
        self.action_f = action_f
        self.policy_f = policy_f
        self.reward_f = reward_f
        self.def_val = def_val
        return None

    def run(self, start_state):
        """
        Function to run the Q-learning algorithm setup in __init__.
        Starting from the start_state state and ends when action_f returns an
        empty list (no new actions can be made)

        """

        curr_state = start_state
        while (pos_actions = self.action_f(curr_state)) != []:
            actions_rewards = zip(pos_actions,
                    [self.reward_f(curr_state, a) for a in pos_actions])
            action_taken = self.policy_f(actions_rewards)
            new_state = self.q_f(current_state, action_taken)
            # CONTINUE HERE
            # FIRST TODO: FIND BEST REWARD OF NEW STATE AND UPDATE REWARD OF
            # CURRENT STATE

        return None
