import instrumento as inst
import matplotlib.pyplot as plt

if __name__ == "__main__":
    guitarra_b5 = inst.Lector.leer_wav('Notas/guitarra-b5.wav', "Guitarra B5")
    guitarra_d5 = inst.Lector.leer_wav('Notas/guitarra-d5.wav', "Guitarra D5")
    guitarra_e6 = inst.Lector.leer_wav('Notas/guitarra-e6.wav', "Guitarra E6")
    guitarra = inst.Instrumento([guitarra_b5, guitarra_d5, guitarra_e6], "Guitarra")

    # plt.figure(1)
    # guitarra_d5.graficar(240)
    # plt.title("Guitarra D5 en Tiempo")
    # plt.figure(2)
    # guitarra_d5.transformarFourier().graficar()
    # plt.title("Guitarra D5 en Frecuencia")
    # plt.show()

    # guitarra.comparar_transformada(1)
    # guitarra.comparar_tiempo(2, 240)
    # plt.show()

    violin_c4 = inst.Lector.leer_wav('Notas/violin-c4.wav', "Violin C4")
    violin_g3 = inst.Lector.leer_wav('Notas/violin-g3.wav', "Violin G3")
    violin_g5 = inst.Lector.leer_wav('Notas/violin-g5.wav', "Violin G5")
    violin = inst.Instrumento([violin_c4, violin_g3, violin_g5], "Violín")

    # plt.figure(1)
    # violin_c4.graficar(240)
    # plt.title("Violin C4 en Tiempo")
    # plt.figure(2)
    # violin_c4.transformarFourier().graficar()
    # plt.title("Violin C4 en Frecuencia")
    # plt.show()

    # violin.comparar_transformada(1)
    # violin.comparar_tiempo(2, 240)
    # plt.show()

    flauta_b5 = inst.Lector.leer_wav('Notas/flauta-b5.wav', "Flauta B5")
    flauta_c4 = inst.Lector.leer_wav('Notas/flauta-c4.wav', "Flauta C4")
    flauta_g6 = inst.Lector.leer_wav('Notas/flauta-g6.wav', "Flauta G6")
    flauta = inst.Instrumento([flauta_b5, flauta_c4, flauta_g6], "Flauta")

    # plt.figure(1)
    # flauta_b5.graficar(240)
    # plt.title("Flauta B5 en Tiempo")
    # plt.figure(2)
    # flauta_b5.transformarFourier().graficar()
    # plt.title("Flauta B5 en Frecuencia")
    # plt.show()

    # flauta.comparar_transformada(1)
    # flauta.comparar_tiempo(2, 240)
    # plt.show()

    oboe_b5 = inst.Lector.leer_wav('Notas/oboe-b5.wav', "Oboe B5")
    oboe_c4 = inst.Lector.leer_wav('Notas/oboe-c4.wav', "Oboe C4")
    oboe_g5 = inst.Lector.leer_wav('Notas/oboe-g5.wav', "Oboe G5")
    oboe = inst.Instrumento([oboe_b5, oboe_c4, oboe_g5], "Oboe")

    # plt.figure(1)
    # oboe_b5.graficar(240)
    # plt.title("Oboe B5 en Tiempo")
    # plt.figure(2)
    # oboe_b5.transformarFourier().graficar()
    # plt.title("Oboe B5 en Frecuencia")
    # plt.show()

    # oboe.comparar_transformada(1)
    # oboe.comparar_tiempo(2, 240)
    # plt.show()

    # comparaciones = inst.Instrumento([guitarra_d5, violin_c4, flauta_b5, oboe_b5], "Comparaciones")
    # comparaciones.comparar_transformada(1)
    # comparaciones.comparar_tiempo(2, 240)
    # plt.show()
