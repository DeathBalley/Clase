import json

RUTA_JSON = "src/datos.json"
ANIO_ACTUAL = 2026


# ---------- LÓGICA ----------

def clasificar_edad(edad):
    if edad < 18 :
        return "Menor"
    elif edad >= 65 :
        return "Jubilado"
    else :
        return "Adulto"


def calcular_edad(anio_nacimiento):
    return ANIO_ACTUAL - anio_nacimiento


def normalizar_nombre(nombre):
    return nombre.strip()


# ---------- JSON (cargar/guardar) ----------

def cargar_personas():
    try:
        archivo = open(RUTA_JSON, "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()

        if type(datos) != list:
            return []
        return datos

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def guardar_personas(personas):
    archivo = open(RUTA_JSON, "w", encoding="utf-8")
    json.dump(personas, archivo, ensure_ascii=False, indent=2)
    archivo.close()


# ---------- OPERACIONES ----------

def existe_nombre(personas, nombre):
    for p in personas:
        if p.get("nombre") == nombre:
            return True
    return False


def mostrar_personas(personas):
    if len(personas) == 0:
        print("No hay personas guardadas.")
        return

    print("Personas:")
    for p in personas:
        nombre = p.get("nombre", "")
        anio = p.get("anio_nacimiento", None)

        # si falta algo (por archivo tocado a mano), no revienta
        if nombre == "" or type(anio) != int:
            print("- (registro inválido)")
            continue

        edad = calcular_edad(anio)
        categoria = clasificar_edad(edad)
        print(f"- {nombre} | {anio} | {edad} años | {categoria}")


def borrar_persona(personas, nombre):
    nuevas = []
    borrado = False

    for p in personas:
        if p.get("nombre") == nombre and not borrado:
            borrado = True
        else:
            nuevas.append(p)

    return nuevas, borrado


def editar_persona(personas, nombre_viejo, nombre_nuevo, anio_nuevo):
    for p in personas:
        if p.get("nombre") == nombre_viejo:
            p["nombre"] = nombre_nuevo
            p["anio_nacimiento"] = anio_nuevo
            return True
    return False


# ---------- PROGRAMA ----------

def main():
    while True:
        print("\n--- MENÚ PERSONAS ---")
        print("1. Añadir persona")
        print("2. Ver personas")
        print("3. Buscar persona por nombre")
        print("4. Borrar persona")
        print("5. Editar persona")
        print("6. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            personas = cargar_personas()

            nombre = normalizar_nombre(input("Nombre: "))
            if nombre == "":
                print("Nombre vacío, cancelado.")
                continue

            if existe_nombre(personas, nombre):
                print("Ese nombre ya existe, cancelado.")
                continue

            try:
                anio = int(input("Año de nacimiento: ").strip())
            except ValueError:
                print("Año inválido, cancelado.")
                continue

            persona = {"nombre": nombre, "anio_nacimiento": anio}
            personas.append(persona)
            guardar_personas(personas)
            print("Persona guardada.")

        elif opcion == "2":
            personas = cargar_personas()
            mostrar_personas(personas)

        elif opcion == "3":
            personas = cargar_personas()
            buscado = normalizar_nombre(input("Nombre a buscar: "))

            encontrado = False
            for p in personas:
                if p.get("nombre") == buscado:
                    anio = p.get("anio_nacimiento", 0)
                    edad = calcular_edad(anio) if type(anio) == int else "?"
                    print(f"Encontrado: {p} | edad: {edad}")
                    encontrado = True
                    break

            if not encontrado:
                print("No existe.")

        elif opcion == "4":
            personas = cargar_personas()
            nombre = normalizar_nombre(input("Nombre a borrar: "))

            personas_nuevas, borrado = borrar_persona(personas, nombre)
            if borrado:
                guardar_personas(personas_nuevas)
                print("Borrado.")
            else:
                print("No existe, no se borró nada.")

        elif opcion == "5":
            personas = cargar_personas()

            viejo = normalizar_nombre(input("Nombre a editar (viejo): "))
            if not existe_nombre(personas, viejo):
                print("No existe.")
                continue

            nuevo = normalizar_nombre(input("Nombre nuevo: "))
            if nuevo == "":
                print("Nombre nuevo vacío, cancelado.")
                continue

            if nuevo != viejo and existe_nombre(personas, nuevo):
                print("Ese nombre nuevo ya existe, cancelado.")
                continue

            try:
                anio_nuevo = int(input("Año de nacimiento nuevo: ").strip())
            except ValueError:
                print("Año inválido, cancelado.")
                continue

            ok = editar_persona(personas, viejo, nuevo, anio_nuevo)
            if ok:
                guardar_personas(personas)
                print("Editado.")
            else:
                print("No se pudo editar (raro, pero posible).")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

main()
