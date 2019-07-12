import sys
import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import scipy.fftpack as sc


# señal es un array de valores
# fs es la frecuencia de muestreo a la cual esta muestreada esa señal
def transformadaFourier(senial, fs):

    numero_muestras = len(senial)

    # fftshift acomoda los valores de manera entendible
    yf = sc.fft(senial)

    xf = sc.fftshift(np.linspace(-fs/2, fs/2, len(yf)))

    return xf,yf

if __name__ == "__main__":
    
    w = wave.open('/Users/paorodrigues/Downloads/354433__mtg__flute-b5.wav', 'r')

    signal = w.readframes(-1)
    signal = np.fromstring(signal, 'Int16')

    fs = w.getframerate()

    #If Stereo
    if w.getnchannels() == 2:
        print('Just mono files')
        sys.exit(0)

    # Time=np.linspace(0, len(signal)/fs, num=len(signal))
    xx = np.linspace(0, len(signal)/fs, num=2000)

    plt.figure(1)
    plt.title('Signal Wave...')
    plt.plot(xx, signal[0:2000])
    plt.show()

    xf, yf = transformadaFourier(signal[0:2000], fs)

    plt.figure(2)
    plt.title('Transformada de Fourier...')
    plt.plot(xf, np.fft.fftshift(yf))
    plt.show()
