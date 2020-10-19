import numpy as np


class RecordHistory(object):
    """History object."""

    def __init__(self, step_record=None):
        self.records = []
        if step_record is not None:
            self.records.append(step_record)

    def append(self, step_record):
        """Append a record to the history."""
        assert step_record is not None
        self.records.append(step_record)
    
    def pop(self, index=-1):
        """Pop the last record of the history."""
        return self.records.pop(index)
    
    def undiscounted_return(self):
        """Get discounted return of the history."""
        undiscounted_return = 0
        for step_record in self.records:
            undiscounted_return += step_record.reward
        return undiscounted_return

    def discounted_return(self, discount):
        """Get discounted return of the history."""
        discounted_return = 0
        factor = 1
        for step_record in self.records:
            discounted_return += factor * step_record.reward
            factor *= discount
        return discounted_return