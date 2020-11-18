class PrivateObservation(object):
    """Private observation object of env: Kuhn Poker.

    A private observation of Kuhn Poker is encoded as a single scalar
    that indicates the hand of a single player.
    """

    __name_dict = {0: 'J', 1: 'Q', 2: 'K'}

    def __init__(self, encode, player=0):
        self.encode = encode
        self.name = PrivateObservation.__name_dict[encode]
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


class PublicObservation(object):
    """Public observation object of env: Kuhn Poker.

    A public observations of Kuhn Poker is encoded as [b1, b2], where
    b1, b2 represent the total bet of two players at the moment.
    """

    def __init__(self, encode):
        self.encode = encode
        self.name = ', '.join(str(x) for x in encode)

    def to_string(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.encode == other.encode
        else:
            return False

    def __ne__(self, other):
        return not self == other
