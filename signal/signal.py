import numpy as np


class Signal:

    def __init__(self, record):
        self.record = record
        self._timeline = None

    @property
    def timeline(self):
        if self._timeline is None:
            self._timeline = np.linspace(0, float(self.record.sig_len) / self.record.fs, self.record.sig_len)
        return self._timeline
