from statistic.step_record import StepRecord
from env.env import Environment
from env.tiger.tiger_state import State
from env.tiger.tiger_action import Action
from env.tiger.tiger_obs import Observation
import numpy as np


class Tiger(Environment):
    """
    Environment: Tiger
    """

    def __init__(self, listen_coefficient=0.75):
        self.name = 'Tiger'
        self.listen_coefficient = listen_coefficient

    def new_initial_state(self):
        """Get a new initial state by certain rules."""

        r = np.random.rand()
        state = State(State.LEFT) if r < 0.5 else State(State.RIGHT)

        return state

    def step(self, state, action):
        """Get step result by given state and action."""

        step_record = StepRecord()

        step_record.state = state
        step_record.action = action

        # Get observation
        if action.value == Action.LISTEN:
            # When listen, get the true state obs with probability listen coefficient
            r = np.random.rand()
            if r < self.listen_coefficient:
                step_record.obs = Observation(state.value)
            else:
                step_record.obs = Observation(1 - state.value)
        else:
            # When open the door, always get the true state
            step_record.obs = Observation(state.value)

        # Get reward
        if action.value == Action.LISTEN:
            step_record.reward = -1
        else:
            step_record.reward = 20 if action.value == state.value else -100

        # Get next state
        if action.value == Action.LISTEN:
            step_record.next_state = State(state.value)
        else:
            step_record.next_state = State(State.TERMINAL)
            # The game is over
            step_record.is_terminal = True

        return step_record
