import instrumento as inst


if __name__ == "__main__":

    violin_c4 = inst.Lector.leer_wav('Notas/violin-c4.wav', "Violin C4")

    violin_c4.graficar()
