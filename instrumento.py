import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import scipy.fftpack as sc


class Senal:
    def __init__(self, titulo, fs, tiempos, amplitudes):
        self.titulo = titulo
        self.fs = fs
        self.tiempos = tiempos
        self.amplitudes = amplitudes

    def graficar(self):
        plt.figure(1)
        plt.title(self.titulo)
        plt.plot(self.tiempos, self.amplitudes)
        plt.show()

    def transformarFourier(self):
        numero_muestras = len(self.amplitudes)
        # fftshift acomoda los valores de manera entendible
        yf = sc.fftshift(sc.fft(self.amplitudes))
        xf = np.linspace(-self.fs/2, self.fs/2, len(yf))

        return Senal(titulo, self.fs, xf, yf)


class Instrumento:
    def __init__(self, senales):
        self.senales = senales


class Lector:
    
    @staticmethod
    def leer_wav(archivo, titulo):
        fs, data = wavfile.read(archivo)
        tiempos = np.linspace(0, len(data)/fs, num=len(data))

        return Senal(titulo, fs, tiempos, data)

