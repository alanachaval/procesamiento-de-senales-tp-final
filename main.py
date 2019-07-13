import instrumento as inst
import matplotlib.pyplot as plt

if __name__ == "__main__":

    #violin_b3 = inst.Lector.leer_wav('Notas/violin-b3.wav', "Violin B3")
    #violin_b5 = inst.Lector.leer_wav('Notas/violin-b5.wav', "Violin B5")
    violin_c4 = inst.Lector.leer_wav('Notas/violin-c4.wav', "Violin C4")
    violin_g3 = inst.Lector.leer_wav('Notas/violin-g3.wav', "Violin G3")
    violin_g5 = inst.Lector.leer_wav('Notas/violin-g5.wav', "Violin G5")
    violin = inst.Instrumento([violin_c4, violin_g3, violin_g5], "Violín")

    flauta_b5 = inst.Lector.leer_wav('Notas/flauta-b5.wav', "Flauta B5")
    flauta_c4 = inst.Lector.leer_wav('Notas/flauta-c4.wav', "Flauta C4")
    flauta_g5 = inst.Lector.leer_wav('Notas/flauta-g5.wav', "Flauta G5")
    flauta = inst.Instrumento([flauta_b5, flauta_c4, flauta_g5], "Flauta")

    trombon_a2 = inst.Lector.leer_wav('Notas/trombon-a2.wav', "Trombon A2")
    trombon_c3 = inst.Lector.leer_wav('Notas/trombon-c3.wav', "Trombon C3")
    trombon_g3 = inst.Lector.leer_wav('Notas/trombon-g3.wav', "Trombon G3")
    trombon = inst.Instrumento([trombon_a2, trombon_c3, trombon_g3], "Trombon")

    violin.comparar_transformada(1)
    flauta.comparar_transformada(2)
    trombon.comparar_transformada(3)

    plt.show()

    violin.comparar_tiempo(1)
    flauta.comparar_tiempo(2)
    trombon.comparar_tiempo(3)

    plt.show()