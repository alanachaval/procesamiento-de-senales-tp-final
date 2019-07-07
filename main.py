import os

import numpy as np
import matplotlib.pyplot as plt

folder = "C:/Alan/Untref/ProcesamientoDeSenales/Final/Data"

# https://physionet.org/physiobank/database/aami-ec13/
# Each recording contains one ECG signal sampled at 720 Hz with 12-bit resolution
fs = 720

for index, filename in enumerate(os.listdir(folder)):
    path = os.path.join(folder, filename)
    values = np.fromfile(path)
    timeline = np.linspace(0, float(len(values)) / fs, len(values))
    fig = plt.figure(index)
    fig.canvas.set_window_title(filename)
    plt.plot(timeline, values)

plt.show()
