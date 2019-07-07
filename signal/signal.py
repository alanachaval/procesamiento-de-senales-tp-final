import numpy as np


class Signal:

    def __init__(self, name, values, fs):
        self.name = name
        self.values = values
        self.fs = fs
        self._timeline = None

    @property
    def timeline(self):
        if self._timeline is None:
            self._timeline = np.linspace(0, float(len(self.values)) / self.fs, len(self.values))
        return self._timeline
