from util.console import console

module = 'STEPRECORD'


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

    def show(self):
        console(3, module, "State: " + self.state.to_string())
        console(3, module, "Action: " + self.action.to_string())
        console(3, module, "Observation: " + self.obs.to_string())
        console(3, module, "Reward: " + str(self.reward))
