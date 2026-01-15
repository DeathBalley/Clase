def main():
    archivo = open("src/datos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        nombre = linea.strip()
        if nombre.startswith("V"):
            print(f"Hola {nombre}")
main()

