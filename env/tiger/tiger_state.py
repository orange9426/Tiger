from env.tiger.tiger_action import Action
from env.tiger.tiger_obs import Observation


class State(object):
    """
    State object of env: Tiger.
    """

    LEFT = 0
    RIGHT = 1
    TERMINAL = 2
    __name_dict = {0: 'left', 1: 'right', 2: 'terminal'}

    def __init__(self, value):
        self.value = value
        self.name = State.__name_dict[value]

    def initial_obs(self):
        return Observation(Observation.UNCLEAR)

    def is_terminal(self):
        return self.value == State.TERMINAL

    def legal_actions(self):
        if self.value == State.TERMINAL:
            return []
        else:
            return [Action(Action.LEFT),
                    Action(Action.RIGHT),
                    Action(Action.LISTEN)]

    def to_string(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False

    def __ne__(self, other):
        return not self == other
