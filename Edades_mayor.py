
#Actividad: Básica
#Hagamos un programa que determine si eres mayor de edad o no utilizando las funciones if y else. 
#Para esto, se debe crear una variable donde el usuario pueda ingresar su edad (utiliza un input 
#para este paso) y el programa despliegue un mensaje que muestre si es mayor de edad (>= 18 años) 
#o menor de edad.

ed1 = int(input('Escribe tu edad: '))

if ed1 >= 18:
    print ("¡Felicidades eres mayor de edad!")
else:
    print("No eres mayor de edad")


#Actividad: Avanzada
#Hagamos un programa que le pida al usuario que ingrese dos nombres con su respectivas edades y muestre 
# quién de ellos es mayor. Para dicha actividad, el usuario debe ingresar dos nombres y dos edades distintas, 
# para que después el programa identifique quién de ellos es mayor e imprima el nombre del mayor, 
# su edad y si es mayor o menor de edad.

nom1 = str(input('Ingresa el primer nombre:'))
ed_1 = int(input('Ingresa la primera edad:'))
nom2 = str(input('Ingresa el segundo nombre: '))
ed_2 = int(input('Ingresa la segunda edad: '))

if ed_1 > ed_2:
    if ed_1 >= 18:
        print(f'{nom1} es mayor con {ed_1} años, y es mayor de edad')
    else:
        print(f'{nom1} es mayor con {ed_1} años, pero es menor de edad')
elif ed_2 > ed_1:
    if ed_2 >= 18:
        print(f'{nom2} es mayor con {ed_2} años, y es mayor de edad')
    else:
        print(f'{nom2} es mayor con {ed_2} años, pero es menor de edad')