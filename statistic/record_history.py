import numpy as np


class History(list):
    """History object to store the step records list as a trajectory.

    This is a list in order of the step records of any trajectories. In FOGs, this
    represents the perfect game state in a game tree, and avoids calculation of
    observations every time the information state is obtained from the history.
    """

    def __init__(self, a=[]):
        super().__init__(a)

    def get_info_state(self):
        """Get the info states of two players corresponding to the history."""

        info_state = (InformationState(player=0), InformationState(player=1))

        for player in [0, 1]:
            # Get the initial obs tuple: (O_priv_0, O_priv_1, O_pub)
            initial_obs = self[0].state.initial_obs()
            info_state[player].append((initial_obs[player], initial_obs[-1]))
            for record in self:
                info_state[player].append(record.action)
                info_state[player].append((record.obs[player], record.obs[-1]))

        return info_state

    def get_public_state(self):
        """Get the public state corresponding to the history."""

        public_state = PublicState()

        # Append the initial public observation
        public_state.append(self[0].state.initial_obs()[-1])
        for record in self:
            public_state.append(record.obs[-1])

        return public_state

    def undiscounted_return(self):
        """Get undiscounted return of the trajectory."""

        undiscounted_return = 0
        for step_record in self:
            undiscounted_return += step_record.reward
        return undiscounted_return

    def discounted_return(self, discount):
        """Get discounted return of the trajectory."""

        discounted_return = 0
        factor = 1
        for step_record in self:
            discounted_return += factor * step_record.reward
            factor *= discount
        return discounted_return

    def __eq__(self, other):
        if isinstance(other, self.__class__) and len(self) == len(other):
            return all([x == y for x, y in zip(self, other)])
        else:
            return False

    def __ne__(self, other):
        return not self == other


class InformationState(list):
    """Represents the node where players make decisions.
    
    This is a sequence of observations and actions of a single player 'i' like
    [O_i^0, a_i^0, O_i^1, a_i^1, ..., O_i^t] in FOGs.
    """

    def __init__(self, a=[], player=0):
        super().__init__(a)
        self.player = player

    def get_public_state(self):
        """Get the public state corresponding to the information state."""
        public_state = PublicState()
        for i, item in enumerate(self):
            if i % 2 == 0:  # for observations
                public_state.append(item[-1])
        return public_state

    def __eq__(self, other):
        if isinstance(other, self.__class__) and len(self) == len(other):
            return all([x == y for x, y in zip(self, other)])
        else:
            return False

    def __ne__(self, other):
        return not self == other


class PublicState(list):
    """Public state object defined in FOGs."""

    def __init__(self, a=[]):
        super().__init__(a)

    def __eq__(self, other):
        if isinstance(other, self.__class__) and len(self) == len(other):
            return all([x == y for x, y in zip(self, other)])
        else:
            return False

    def __ne__(self, other):
        return not self == other
