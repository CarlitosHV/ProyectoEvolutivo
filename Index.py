import numpy as np
import Insumos as ins
import Recipes as rec
import random
import matplotlib.pyplot as plt

# Mi configuración del individuo e instancias
num_recipes = 19
num_persons = 20
recipes = rec.Recipes()
supplies = ins.Insumos()
maximo = 0
num_generaciones = 5
tam_torneo = 2
puntos_cruce = [2, 8, 14, 18]

# Población de prueba
population_test = [
    [5, 7, 8, 8, 7, 7, 2, 5, 7, 6, 1, 5, 2, 4, 7, 7, 0, 2, 9],
    [3, 0, 0, 7, 4, 9, 5, 0, 3, 9, 5, 7, 3, 2, 0, 4, 4, 1, 2],
    [1, 5, 8, 9, 8, 0, 3, 1, 8, 4, 9, 5, 0, 5, 9, 1, 1, 2, 2],
    [0, 4, 7, 1, 7, 1, 5, 9, 2, 5, 6, 1, 6, 3, 8, 5, 5, 3, 2],
    [4, 8, 3, 5, 6, 5, 5, 7, 6, 2, 4, 2, 7, 5, 4, 1, 8, 8, 2],
    [6, 9, 4, 9, 7, 6, 0, 2, 5, 3, 6, 4, 4, 8, 3, 6, 4, 4, 7],
    [2, 0, 0, 9, 9, 6, 1, 9, 0, 9, 0, 9, 6, 1, 4, 3, 3, 1, 0],
    [3, 3, 6, 0, 4, 9, 4, 5, 7, 3, 0, 0, 4, 2, 6, 0, 8, 3, 1],
    [4, 3, 6, 2, 7, 6, 8, 8, 7, 2, 4, 5, 0, 8, 0, 3, 6, 7, 4],
    [1, 7, 5, 1, 9, 1, 0, 3, 2, 2, 5, 8, 7, 8, 8, 5, 6, 4, 1],
    [4, 9, 5, 2, 7, 9, 4, 0, 7, 9, 0, 4, 1, 2, 3, 9, 4, 0, 3],
    [1, 4, 4, 6, 1, 4, 8, 6, 3, 2, 5, 6, 8, 1, 6, 7, 7, 5, 8],
    [6, 5, 0, 2, 3, 9, 2, 3, 5, 7, 8, 9, 9, 2, 7, 8, 7, 0, 6],
    [4, 1, 0, 8, 5, 0, 7, 3, 4, 1, 8, 9, 2, 5, 0, 4, 4, 8, 2],
    [4, 3, 4, 3, 2, 4, 3, 3, 7, 0, 9, 3, 8, 5, 4, 1, 9, 7, 0],
    [1, 6, 8, 1, 2, 6, 1, 4, 8, 9, 1, 4, 1, 2, 2, 5, 1, 7, 1],
    [1, 2, 7, 7, 1, 5, 7, 9, 6, 2, 8, 3, 1, 3, 6, 1, 9, 6, 6],
    [5, 8, 1, 2, 8, 5, 1, 0, 6, 4, 2, 2, 0, 8, 0, 9, 6, 2, 0],
    [2, 7, 1, 4, 7, 3, 7, 7, 7, 2, 6, 2, 2, 9, 6, 0, 3, 3, 8],
    [2, 5, 0, 3, 4, 3, 4, 9, 2, 7, 7, 1, 8, 3, 0, 4, 0, 1, 7],
]
population = np.array(population_test)

def funcion_aptitud(individuo):
    ganancias = 0
    merma = 0
    tiempo_total = 0

    # Calculo las ganancias y el tiempo total
    for i, (nombre_receta, cantidad) in enumerate(zip(recipes.recipes.keys(), individuo)):
        ganancias += cantidad * recipes.obtener_recipes(nombre_receta)['Precio']
        tiempo_total += cantidad * recipes.obtener_recipes(nombre_receta)['Tiempo elaboración']

    # Si el tiempo total excede el límite, penalizamos la aptitud
    if tiempo_total / 3 > 240:
        return -1

    # Calculo la merma
    insumos_usados = {}
    for i, (nombre_receta, cantidad) in enumerate(zip(recipes.recipes.keys(), individuo)):
        for insumo, cantidad_insumo in recipes.obtener_recipes(nombre_receta).items():
            if insumo not in insumos_usados:
                insumos_usados[insumo] = 0
            insumos_usados[insumo] += cantidad * cantidad_insumo

    for insumo, cantidad in insumos_usados.items():
        if insumo != 'Precio' and insumo != 'Costo elaboración' and insumo != 'Tiempo elaboración':
            if cantidad > supplies.obtener_insumo(insumo)['Cantidad']:
                merma += (cantidad - supplies.obtener_insumo(insumo)['Cantidad']) * supplies.obtener_insumo(insumo)[
                    'Precio']

    # La aptitud es igual a la merma menos la ganancia
    aptitud = merma - ganancias

    return aptitud


def seleccion_torneo(poblacion, funcion_aptitud, tam_torneo=3):
    # Selecciona aleatoriamente 'tam_torneo' individuos de la población
    seleccionados = random.sample(poblacion, tam_torneo)

    # Evalúa la aptitud de los individuos seleccionados
    aptitudes = [funcion_aptitud(individuo) for individuo in seleccionados]

    # Obtiene el índice del individuo con la mejor aptitud
    indice_ganador = aptitudes.index(max(aptitudes))

    # Retorna el individuo ganador del torneo
    return seleccionados[indice_ganador]


def cruce_multipunto(padre1, padre2, puntos):
    # Asegura que los puntos de cruce estén ordenados
    puntos = sorted(puntos)

    # Inicializa la descendencia como listas vacías
    hijo1 = []
    hijo2 = []

    # Realiza el cruce en cada segmento definido por los puntos de cruce
    for i in range(len(puntos) - 1):
        if i % 2 == 0:
            # En segmentos pares, el hijo1 recibe genes del padre1 y el hijo2 del padre2
            hijo1.extend(padre1[puntos[i]:puntos[i + 1]])
            hijo2.extend(padre2[puntos[i]:puntos[i + 1]])
        else:
            # En segmentos impares, el hijo1 recibe genes del padre2 y el hijo2 del padre1
            hijo1.extend(padre2[puntos[i]:puntos[i + 1]])
            hijo2.extend(padre1[puntos[i]:puntos[i + 1]])

    # Asegura que los últimos genes sean añadidos a la descendencia
    if len(puntos) % 2 == 0:
        hijo1.extend(padre1[puntos[-1]:])
        hijo2.extend(padre2[puntos[-1]:])
    else:
        hijo1.extend(padre2[puntos[-1]:])
        hijo2.extend(padre1[puntos[-1]:])

    return hijo1, hijo2

# Inicializa listas para almacenar el promedio y la mejor aptitud de cada generación
promedios = []
mejores = []

for generacion in range(num_generaciones):
    print(f'Generación {generacion + 1}')

    # Calcula la aptitud de cada individuo en la población
    aptitudes = [funcion_aptitud(individuo) for individuo in population_test]

    # Calcula el promedio y la mejor aptitud de la generación actual
    promedio = sum(aptitudes) / len(aptitudes)
    mejor = max(aptitudes)

    # Añade el promedio y la mejor aptitud a las listas correspondientes
    promedios.append(promedio)
    mejores.append(mejor)

    print(f'Promedio de aptitud: {promedio:.2f}')
    print(f'Mejor aptitud: {mejor:.2f}')

    # Crea una nueva población a través de la selección y el cruce
    nueva_poblacion = []
    for _ in range(num_persons // 2):
        # Selecciona dos padres utilizando el torneo de selección
        padre1 = seleccion_torneo(population_test, funcion_aptitud, tam_torneo)
        padre2 = seleccion_torneo(population_test, funcion_aptitud, tam_torneo)

        # Crea dos hijos a través del cruce multipunto
        hijo1, hijo2 = cruce_multipunto(padre1, padre2, puntos_cruce)

        # Añade los hijos a la nueva población
        nueva_poblacion.extend([hijo1, hijo2])

    # Reemplaza la población antigua con la nueva población
    population_test = nueva_poblacion

# Crea una gráfica de líneas con los promedios y las mejores aptitudes
plt.plot(promedios, label='Promedio')
plt.plot(mejores, label='Mejor')
plt.xlabel('Generación')
plt.ylabel('Aptitud')
plt.legend()
plt.show()
