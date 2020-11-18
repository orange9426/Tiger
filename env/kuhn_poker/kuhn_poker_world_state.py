from env.kuhn_poker.kuhn_poker_action import Action
from env.kuhn_poker.kuhn_poker_obs import PrivateObservation
from env.kuhn_poker.kuhn_poker_obs import PublicObservation


class WorldState(object):
    """World state object of env: Kuhn Poker.

    A world state of Kuhn Poker is encoded as [[h1, h2], [b1, b2], turn],
    where h1, h2 represent the hands of two players respectively, and
    b1, b2 represent the total bet of two players. 'turn' indicates which
    player is currently playing and when turn == -1, it means that the
    game is over.
    """

    __hand_dict = {0: 'J', 1: 'Q', 2: 'K'}

    def __init__(self, encode):
        self.encode = encode
        self.name = '[%s, %s], [%d, %d], %d' % \
            (WorldState.__hand_dict[encode[0][0]],
             WorldState.__hand_dict[encode[0][1]],
             encode[1][0], encode[1][1], encode[2])
        self.player = encode[-1]

    def is_terminal(self):
        return self.encode[-1] == -1

    def current_player(self):
        return self.player

    def initial_obs(self):
        return PrivateObservation(self.encode[0][0], 0), \
            PrivateObservation(self.encode[0][1], 1), \
            PublicObservation([1, 1])

    def legal_actions(self):
        return [] if self.encode[-1] == -1 else \
            [Action(0, self.encode[-1]), Action(1, self.encode[-1])]

    def to_string(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.encode == other.encode
        else:
            return False

    def __ne__(self, other):
        return not self == other
