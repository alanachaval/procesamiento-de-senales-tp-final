import matplotlib.pyplot as plt

from datapreparation.file_reader import FileReader

folder = "C:/Alan/Untref/ProcesamientoDeSenales/Final/Data"

for index, signal in enumerate(FileReader(folder)):
    fig = plt.figure(index)
    fig.canvas.set_window_title(signal.name)
    plt.plot(signal.timeline, signal.values)

plt.show()
