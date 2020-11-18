class Action(object):
    """Action object of env: Kuhn Poker.

    An action of Kuhn Poker is encoded as a single scalar that is
    0, 1 when act pass, bet respetively.
    """

    __name_dict = {0: 'pass', 1: 'bet'}

    def __init__(self, encode, player=0):
        self.encode = encode
        self.name = Action.__name_dict[encode]
        self.player = player

    def to_string(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.encode == other.encode
        else:
            return False

    def __ne__(self, other):
        return not self == other
