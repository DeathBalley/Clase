anio_actual = date (year)
anio_nacimiento =int(input ("¿En que año naciste?"))
edad = anio_actual - anio_nacimiento

if edad < 18 :
    print ("Eres menor de edad")
elif edad >= 65 :
    print ("Eres jubilado")
else :
    print ("Eres adulto")