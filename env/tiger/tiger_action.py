class Action(object):
    """
    Action object of env: Tiger.
    """

    LEFT = 0
    RIGHT = 1
    LISTEN = 2
    __name_dict = {0: 'left', 1: 'right', 2: 'listen'}

    def __init__(self, value):
        self.value = value
        self.name = Action.__name_dict[value]

    def to_string(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False

    def __ne__(self, other):
        return not self == other
