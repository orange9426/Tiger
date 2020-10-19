import numpy as np


class StepRecord(object):
    """
     Represents the records of a complete step in the model, including the next state,
     * observation, and reward
     *
     * For convenience, this also includes the action taken, and a boolean flag representing
     * whether or not the recording next state is a terminal state.
    """

    def __init__(self):
        self.state = None
        self.action = None
        self.obs = None
        self.reward = 0
        self.next_state = None
        self.is_terminal = False

    def print_step_record(self):
        print("------- Step Record --------")
        print("Action: ", end=' ')
        self.action.print_action()
        print("Observation: ", end=' ')
        self.obs.print_observation()
        print("Reward: ", end=' ')
        print(self.reward)
        print("Next state: ", end=' ')
        self.next_state.print_state()
        print("Is terminal: ", end=' ')
        print(self.is_terminal)
