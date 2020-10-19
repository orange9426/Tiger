import abc


class Environment(object):
    """Abstract class of Environment."""

    @abc.abstractmethod
    def new_initial_state(self):
        pass

    @abc.abstractmethod
    def step(self):
        pass
