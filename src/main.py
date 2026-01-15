def main():
    archivo = open("src/datos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        print(linea)

main()
