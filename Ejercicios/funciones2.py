import random
import math

# Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). Luego:
#
# Muestre la lista
# El usuario ingresa debe ingresar un valor un valor. El programa debe informar cuántos valores de la lista son mayores a dicho valor, para eso debe utilizar una función.
# La función debe recibir como argumentos la lista y un entero, y debe retornar la cantidad de valores de la lista mayores a dicho entero.
# Crear una función que calcule el promedio de la lista y utilizarla.
# Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.

l = []
for x in range(10):
    l.append(random.randint(1, 21))

print(l)


def buscarMayores(lista, num):
    contador = 0
    for x in lista:
        if x > num:
            contador += 1
    return contador


numero = int(input("Ingrese un número entero: "))

mayores = buscarMayores(l, numero)

print(f'La cantidad de números generados mayores al que ingresó es: {mayores}')


def promedio(lista):
    suma = 0
    cont = 0
    for x in lista:
        suma+=x
        cont+=1
    prom = suma/cont
    return prom


prom = promedio(l)

print(f'El promedio es: {prom}')


def menor_mayor(lista):
    menor = min(lista)
    mayor = max(lista)
    return menor, mayor


(menor, mayor) = menor_mayor(l)

print(f'El mayor es {mayor} y el menor es {menor}')
