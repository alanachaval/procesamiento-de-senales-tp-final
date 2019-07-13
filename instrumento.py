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

    def graficar(self, porcentaje=1):
        muestras = int(porcentaje * len(self.tiempos))
        plt.plot(self.tiempos[0:muestras], self.amplitudes[0:muestras])
        return self

    def transformarFourier(self):
        numero_muestras = len(self.amplitudes)
        # fftshift acomoda los valores de manera entendible
        yf = sc.fftshift(sc.fft(self.amplitudes))
        xf = np.linspace(-self.fs/2, self.fs/2, len(yf))

        return Senal(self.titulo, self.fs, xf, np.abs(yf))


class Instrumento:
    def __init__(self, senales, nombre):
        self.senales = senales
        self.nombre = nombre

    def comparar_transformada(self, fig_id):
        plt.figure(fig_id)
        leyenda = list()
        for senal in self.senales:
            leyenda.append(senal.transformarFourier().graficar().titulo)

        plt.legend(leyenda, loc='upper right')
        plt.title(self.nombre + " en Frecuencia")
    
    def comparar_tiempo(self, fig_id):
        plt.figure(fig_id)
        leyenda = list()
        for senal in self.senales:
            leyenda.append(senal.graficar(0.005).titulo)

        plt.legend(leyenda, loc='upper right')
        plt.title(self.nombre + " en Tiempo")

class Lector:
    
    @staticmethod
    def leer_wav(archivo, titulo):
        fs, data = wavfile.read(archivo)
        muestras = int(1*fs)
        data = data[0:muestras]
        tiempos = np.linspace(0, len(data)/fs, num=len(data))

        return Senal(titulo, fs, tiempos, data)

