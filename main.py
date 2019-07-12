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
    yf = sc.fftshift(sc.fft(senial))

    xf = np.linspace(-fs/2, fs/2, len(yf))

    return xf,yf


def two_channels(signal):

    print(signal.shape)
    signal1 = signal[:0]
    signal2 = signal[:1]

    fs = w.getframerate()

    xx = np.linspace(0, len(signal1)/fs, num=len(signal1))
    #xx = np.linspace(0, len(signal)/fs, num=2000)

    plt.figure(1)
    plt.title('Signal1')
    #plt.plot(xx, signal[0:2000])
    plt.plot(xx, signal1)
    plt.show()

    #xf, yf = transformadaFourier(signal[0:2000], fs)
    xf, yf = transformadaFourier(signal1, fs)

    plt.figure(2)
    plt.title('Transformada de Fourier...')
    plt.plot(xf, np.fft.fftshift(yf))
    plt.show()

def read_file(file):
    w = wave.open(file, 'r')

    signal = w.readframes(-1)
    signal = np.fromstring(signal, 'Int16')

    fs = w.getframerate()

    # #If Stereo
    # if w.getnchannels() == 2:
    #     print('Just mono files')
    #     sys.exit(0)

    xx = np.linspace(0, len(signal)/fs, num=len(signal))
    #xx = np.linspace(0, len(signal)/fs, num=2000)

    return xx, signal, fs


if __name__ == "__main__":
    
    x1, y1, fs1 = read_file('/Users/paorodrigues/Downloads/NotasRecortadas/355808__mtg__violin-c4_2.wav')
    x2, y2, fs2 = read_file('/Users/paorodrigues/Downloads/NotasRecortadas/355807__mtg__violin-g5_2.wav')

    plt.figure(1)
    plt.title('Signal Wave...')
    #plt.plot(xx, signal[0:2000])
    plt.plot(x1, y1)
    
    plt.plot(x2, y2)
    plt.show()

    xf1, yf1 = transformadaFourier(y1, fs1)

    plt.figure(2)
    plt.title('Transformada de Fourier...')
    plt.plot(xf1, np.abs(yf1))

    #xf, yf = transformadaFourier(signal[0:2000], fs)
    xf2, yf2 = transformadaFourier(y2, fs2)

    plt.figure(2)
    plt.title('Transformada de Fourier...')
    plt.plot(xf2, np.abs(yf2))
    plt.show()

    #two_channels(signal)

