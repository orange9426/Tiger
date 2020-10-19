import abc


class Solver(object):
    """Abstract class of solver."""

    @abc.abstractmethod
    def reset_for_epoch(self):
        pass

    @abc.abstractmethod
    def solve_game(self):
        pass
