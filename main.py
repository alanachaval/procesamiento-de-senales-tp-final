import numpy as np
import matplotlib.pyplot as plt

from datapreparation.file_reader import FileReader

folder = "C:/Alan/Untref/ProcesamientoDeSenales/Final/Data"

for index, signal in enumerate(FileReader(folder)):
    timeline = np.linspace(0, float(len(signal.values)) / signal.fs, len(signal.values))
    fig = plt.figure(index)
    fig.canvas.set_window_title(signal.name)
    plt.plot(timeline, signal.values)

plt.show()
