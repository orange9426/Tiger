class Observation(object):
    """
    Observation object of env: Tiger.
    """

    LEFT = 0
    RIGHT = 1
    UNCLEAR = 2
    __name_dict = {0: 'left', 1: 'right', 2: 'unclear'}

    def __init__(self, value):
        self.value = value
        self.name = Observation.__name_dict[value]

    def to_string(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False

    def __ne__(self, other):
        return not self == other
