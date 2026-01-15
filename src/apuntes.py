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

