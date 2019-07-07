import os

import numpy as np
import pandas as pd

from signal.signal import Signal


class FileReader:

    def __init__(self, data_folder):
        self.data_folder = data_folder

    def __iter__(self):
        return map(self.read_file, filter(lambda x: x.endswith('.hea'), os.listdir(self.data_folder)))

    def read_file(self, header_name):
        # Example of a header file:
        #
        # aami4a 1 720 65211
        # aami4a.dat 16 80 12 2048 2040 15234 0 ECG
        # # ANSI/AAMI EC13-1992, Figure 4a, 1x.
        header_path = os.path.join(self.data_folder, header_name)
        header = pd.read_csv(header_path, sep=" ", names=[0, 1, 2, 3, 4, 5, 6, 7, 8])
        data_name = header.loc[1][0]
        data_path = os.path.join(self.data_folder, data_name)
        data = np.fromfile(data_path)
        fs = int(header.loc[0][2])
        signal_name = header[0][0]
        return Signal(signal_name, data, fs)
