import sys

import matplotlib.pyplot as plt

from datapreparation.file_reader import FileReader

folder = sys.argv[1]

databases = ['aami-ec13', 'edb', 'ltstdb', 'mitdb']

for index, signal in enumerate(FileReader(folder, databases[0])):
    fig = plt.figure(index)
    fig.canvas.set_window_title(signal.record.record_name)
    plt.plot(signal.timeline, signal.record.p_signal)

plt.show()
