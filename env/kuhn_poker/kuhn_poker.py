from statistic.step_record import StepRecord

from env.env import Environment
from env.kuhn_poker.kuhn_poker_world_state import WorldState
from env.kuhn_poker.kuhn_poker_action import Action
from env.kuhn_poker.kuhn_poker_obs import PrivateObservation
from env.kuhn_poker.kuhn_poker_obs import PublicObservation

import numpy as np
import copy


class KuhnPoker(Environment):
    """Environment class: Kuhn Poker

    Define the Kuhn Poker environment as a FOG.
    Replace chance nodes with transition probabilities.
    """

    def __init__(self):
        """Init Kuhn Poker class with naming."""

        self.name = 'Kuhn Poker'
        self.multi_agent = True

    def new_initial_state(self):
        """Get a new initial world state by initial world_state distribution."""

        r = np.random.randint(6)
        w_encode = [[r % 3, (r % 3 + r // 3 + 1) % 3], [1, 1], 0]
        return WorldState(w_encode)

    def initial_states(self):
        """Return two lists of the initial states and the probability."""

        states_list = [WorldState([[i, (i + j) % 3], [1, 1], 0])
                       for i in range(3) for j in range(1, 3)]
        prob_list = [1 / len(states_list) for x in states_list]
        return states_list, prob_list

    def get_all_states(self):
        """Return a list of all possible world states."""

        initial_states_list, _ = self.initial_states()
        hands_list = [w.encode[0].copy() for w in initial_states_list]
        states_list = []
        for hands in hands_list:
            states_list += [WorldState([hands, bets, 0]) for bets in [[1, 1], [1, 2]]] \
                + [WorldState([hands, bets, 1]) for bets in [[1, 1], [2, 1]]]

        return states_list

    def step(self, world_state, action):
        """Get the step result given a world state and an action."""

        step_record = StepRecord()

        step_record.state = world_state
        step_record.action = action

        # Get next world state and rewards
        w_encode = copy.deepcopy(world_state.encode)
        if action.encode == 0:  # pass
            # The game will not end after 'pass' only if at the beginning
            if w_encode[1] == [1, 1] and w_encode[-1] == 1:
                w_encode[-1] = 1 - w_encode[-1]  # opponent's turn
                step_record.reward = 0
            else:  # the game is over
                w_encode[-1] = -1  # terminal
                step_record.is_terminal = True
                if w_encode[1] == [1, 1]:  # all pass
                    step_record.reward = 1 if w_encode[0][0] > w_encode[0][1] else -1
                else:
                    # The player who passes will lose
                    step_record.reward = 1 if action.player == 1 else -1
        else:  # bet
            w_encode[1][action.player] += 1  # the bet of current player +1
            # The game will end after 'bet' only if all bet
            if w_encode[1] == [2, 2]:
                w_encode[-1] = -1  # terminal
                step_record.is_terminal = True
                step_record.reward = 2 if w_encode[0][0] > w_encode[0][1] else -2
            else:
                w_encode[-1] = 1 - w_encode[-1]  # opponent's turn
        step_record.next_state = WorldState(w_encode)

        # Get observation
        # Observations always match the world state
        step_record.obs = (PrivateObservation(w_encode[0][0], 0),
                           PrivateObservation(w_encode[0][1], 1),
                           PublicObservation(w_encode[1]))

        return step_record
