RUTA_ARCHIVO = "src/datos.txt"

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
