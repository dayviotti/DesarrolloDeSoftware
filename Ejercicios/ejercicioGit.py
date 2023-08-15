from math import isnan

valor1 = float(input("Ingrese el 1° valor: "))
valor2 = float(input("Ingrese el 2° valor: "))

print("Menú:")
print("1. Ingresar valor 1")
print("2. Ingresar valor 2")
print("3. Mostrar suma")
print("4. Mostrar resta")
print("5. Mostrar multiplicación")
print("6. Mostrar división")
print("7. Salir\n\n")
opcion = int(input("Elija una opción:"))

while opcion != 7:
    if opcion == 1:
        valor1 = float(input('Ingrese el valor 1: '))
    elif opcion == 2:
        valor2 = float(input('Ingrese el valor 2: '))
    elif opcion == 3:
        suma = valor1 + valor2
        print(f'La suma es: {suma}')
    elif opcion == 4:
        resta = valor1 - valor2
        print(f'La resta es: {resta}')
    elif opcion == 5:
        multiplicacion = valor1*valor2
        print(f'La multiplicación es: {multiplicacion}')
    elif opcion == 6:
        division = valor1/valor2
        print(f'La división es: {division}')
    else:
        print(f"La opción {opcion} no existe.")

    opcion = int(input("Elija una opción:"))

print("No vemo en Disney")