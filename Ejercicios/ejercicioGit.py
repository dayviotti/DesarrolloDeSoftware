from math import isnan
def validar(v1,v2):
    existeValor1 = False
    existeValor2 = False
    if isnan(valor1):
        existeValor1 = True
    if isnan(valor2):
        existeValor2 = True
    if existeValor1 and existeValor2:
        return True
    else:
        if existeValor1:
            print("Todavía no ingresó el valor 2.")
        elif existeValor2:
            print("Todavía no ingresó el valor 1.")
        else:
            print("Todavía no ingresó ninguno de los dos valores.")
        return False


print("Menú:")
print("1. Ingresar valor 1")
print("2. Ingresar valor 2")
print("3. Mostrar suma")
print("4. Mostrar resta")
print("5. Mostrar multiplicación")
print("6. Mostrar división")
print("7. Salir\n\n")
opcion = input(int("Elija una opción:"))

while opcion != 7:
    if opcion == 1:
        valor1 = input(float('Ingrese el valor 1: '))
    elif opcion == 2:
        valor2 = input(float('Ingrese el valor 2: '))
    elif opcion == 3:
        if validar(valor1, valor2):
            suma = valor1 + valor2
            print(f'La suma es: {suma}')
    elif opcion == 4:
        if validar(valor1, valor2):
            resta = valor1 - valor2
            print(f'La resta es: {resta}')
    elif opcion == 5:
        if validar(valor1, valor2):
            multiplicacion = valor1*valor2
            print(f'La multiplicación es: {multiplicacion}')
    elif opcion == 6:
        if validar(valor1, valor2):
            division = valor1/valor2
            print(f'La división es: {division}')
    else:
        print(f"La opción {opcion} no existe.")

    opcion = input(int("Elija una opción:"))

