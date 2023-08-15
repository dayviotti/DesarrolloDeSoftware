import generarAtletas

# Utilizar la función anterior para generar y almacenar una lista de atletas
# Escribir una función que reciba la lista de atletas e imprima una línea por cada atleta respetando el siguiente formato: "<num_atleta> - : (<tiempo_llegada> segundos)", donde <num_atleta> es el número del atleta, su nombre y <tiempo_llegadad> su tiempo de llegada.
# Escribir una función que devuelva el número del atleta que resultó ganador.
# Escribir una función que, recibiendo el número de atleta de un competidor, devuelva todos sus datos (nombre, número y tiempo de llegadad).
# OPCIONAL: Escribir una función que devuelva una tupla con los números de los 3 atletas que entraron al podio de ganadores en orden de llegada.

atletas = generarAtletas.generar_lista_de_atletas()

def mostrar_atleta(lista):
    for x in lista:
        print(f'#{x["numero"]} {x["nombre"]} -: ({x["tiempo_llegada"]} segundos)')

def buscarGanador(lista):
    cont = 0
    for i in lista:
        if cont == 0:
            atletaGanador = i['numero']
            tiempo = i['tiempo_llegada']
        else:
            if i['tiempo_llegada']<tiempo:
                atletaGanador = i['numero']
        cont+=1
    return atletaGanador

def mostrarDatos(lista):
    ganador = buscarGanador(lista)
    for j in lista:
        if j['numero'] == ganador:
            nombre = j['nombre']
            tiempo_llegada = j['tiempo_llegada']
    return nombre, ganador, tiempo_llegada




