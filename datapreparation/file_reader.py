import os
import numpy as np

from signal.signal import Signal


class FileReader:

    def __init__(self, data_folder):
        self.data_folder = data_folder

    def __iter__(self):
        return map(self.read_file, os.listdir(self.data_folder))

    def read_file(self, filename):
        path = os.path.join(self.data_folder, filename)
        values = np.fromfile(path)
        # https://physionet.org/physiobank/database/aami-ec13/
        # Each recording contains one ECG signal sampled at 720 Hz with 12-bit resolution
        fs = 720
        return Signal(filename, values, fs)
