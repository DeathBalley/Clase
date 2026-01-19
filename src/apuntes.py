anio_actual = date (year)
#para hacer inputs
    anio_nacimiento =int(input ("¿En que año naciste?")) 

edad = anio_actual - anio_nacimiento

#if 
    if edad < 18 :
        print ("Eres menor de edad")
    elif edad >= 65 :
        print ("Eres jubilado")
    else :
        print ("Eres adulto")

#bucles
    contador = 1

    while contador <= 10:
        print (contador)
        contador = contador + 1

    for i in range(10):
        print(i + 1)

    i = 1

    for i <= 10:
        print (i)
        i = i + 1

#listas index
    nombres = ["Victor","Jorge","Alberto"]
    for nombre in nombres:
        print (nombre)

    edades = [12, 18, 25, 67, 15, 80]

    for edad in edades :
        if edad < 18 :
            print ("Menor")
        elif edad >= 65 :
            print ("Jubilado")
        else :
            print ("Adulto") 

    for edad in edades :
        if edad < 18 :
            print(f"{edad} -> Menor")
        elif edad >= 65 :
            print(f"{edad} -> Jubilado")
        else :
            print(f"{edad} -> Adulto")


#Ejercicio 1
    anio_actual = 2026
    anio_nacimiento =int(input ("¿En que año naciste?"))
    edad = anio_actual - anio_nacimiento


    def clasificar_edad(edad):
    
        if edad < 18 :
            return "Menor"
        elif edad >= 65 :
            return "Jubilado"
        else :
            return "Adulto" 
                

    def main():
        anio_actual = 2026
        anio_nacimiento =int(input ("¿En que año naciste?"))
        edad = anio_actual - anio_nacimiento
        
        print(f"Tienes {edad}. Eres {clasificar_edad(edad)}")

    main()

#Ejercicio 1 version gpt
    def clasificar_edad(edad):
        if edad < 18 :
            return "Menor"
        elif edad >= 65 :
            return "Jubilado"
        else :
            return "Adulto"

    def main():
        anio_actual = 2026
        anio_nacimiento = int(input("¿En qué año naciste? "))
        edad = anio_actual - anio_nacimiento

        categoria = clasificar_edad(edad)
        print(f"Tienes {edad} años -> {categoria}")

    main()

#crear txt para almacenar datos
    def main():
        nombre = input("Escribe un nombre: ")

        archivo = open("src/datos.txt", "a")
        archivo.write(nombre + "\n")
        archivo.close()

        print("Nombre guardado")

    main()

#comprobar los datos del txt 
    def main():
        archivo = open("src/datos.txt", "r")
        contenido = archivo.read()
        archivo.close()

        print("Contenido del archivo:")
        print(contenido)

    main()

    def main():
        archivo = open("src/datos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            nombre = linea.strip()
            print(f"Hola {nombre}")

    main()
    #forma limpia de comprobar archivos
    with open("src/datos.txt", "r") as archivo:
        for linea in archivo:
            nombre = linea.strip()
            if nombre.startswith("V"):
                print(f"Hola {nombre}")

#ejercicio 2
    def main():
        archivo = open("src/datos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            nombre = linea.strip()
            if nombre.startswith("V"):
                print(f"Hola {nombre}")
    main()

#meter y mirar datos
    def guardar_nombre(nombre):
        archivo = open("src/datos.txt", "a")
        archivo.write(nombre + "\n")
        archivo.close()

    def main():
        while True:
            print("1. Añadir nombre")
            print("2. Ver nombres")
            print("3. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                nombre = input("Escribe un nombre: ")
                guardar_nombre(nombre)
                print("Nombre guardado")

            elif opcion == "3":
                print("Saliendo...")
                break

            else:
                print("Opción no implementada todavía")

    main()

# --------- ARCHIVO: escribir / leer / borrar ---------

def guardar_nombre(nombre, evitar_duplicados=True):
    nombre = nombre.strip()

    # No guardamos nombres vacíos
    if nombre == "":
        print("No se ha guardado: el nombre está vacío.")
        return

    if evitar_duplicados:
        nombres_existentes = leer_nombres()
        if nombre in nombres_existentes:
            print("No se ha guardado: ese nombre ya existe.")
            return

    archivo = open(RUTA_ARCHIVO, "a")
    archivo.write(nombre + "\n")
    archivo.close()

    print("Nombre guardado.")


def leer_nombres():
    # Si el archivo no existe todavía, lo creamos vacío.
    try:
        archivo = open(RUTA_ARCHIVO, "r")
    except FileNotFoundError:
        archivo = open(RUTA_ARCHIVO, "w")
        archivo.close()
        return []

    lineas = archivo.readlines()
    archivo.close()

    nombres = []
    for linea in lineas:
        nombre = linea.strip()
        if nombre != "":
            nombres.append(nombre)

    return nombres


def borrar_todos():
    archivo = open(RUTA_ARCHIVO, "w")
    archivo.write("")  # deja el archivo vacío
    archivo.close()
    print("Archivo borrado: ya no hay nombres guardados.")


# --------- LÓGICA: mostrar / filtrar ---------

def mostrar_nombres(nombres):
    if len(nombres) == 0:
        print("No hay nombres para mostrar.")
        return

    print("Nombres:")
    for nombre in nombres:
        print(f"- {nombre}")


def filtrar_por_inicial(nombres, inicial):
    inicial = inicial.strip()
    if inicial == "":
        return nombres

    # Para que no dependa de mayúsculas/minúsculas:
    ini = inicial[0].lower()

    filtrados = []
    for nombre in nombres:
        if nombre.lower().startswith(ini):
            filtrados.append(nombre)

    return filtrados


# --------- PROGRAMA PRINCIPAL ---------

def main():
    while True:
        print("\n--- MENÚ ---")
        print("1. Añadir nombre")
        print("2. Ver nombres")
        print("3. Ver nombres filtrados por inicial")
        print("4. Ver nombres ordenados A-Z")
        print("5. Borrar todos los nombres")
        print("6. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Escribe un nombre: ")
            guardar_nombre(nombre, evitar_duplicados=True)

        elif opcion == "2":
            nombres = leer_nombres()
            mostrar_nombres(nombres)

        elif opcion == "3":
            nombres = leer_nombres()
            inicial = input("¿Qué inicial quieres (por ejemplo V)? ")
            nombres_filtrados = filtrar_por_inicial(nombres, inicial)
            mostrar_nombres(nombres_filtrados)

        elif opcion == "4":
            nombres = leer_nombres()
            nombres_ordenados = sorted(nombres)  # orden alfabético
            mostrar_nombres(nombres_ordenados)

        elif opcion == "5":
            confirmacion = input("¿Seguro que quieres borrar TODO? (s/n): ").strip().lower()
            if confirmacion == "s":
                borrar_todos()
            else:
                print("Cancelado.")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Elige un número del 1 al 6.")


main()

