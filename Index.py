import numpy as np
import Insumos as ins
import Recipes as rec
import random
import matplotlib.pyplot as plt

# Mi configuración del individuo e instancias
num_recipes = 19
num_persons = 10
recipes = rec.Recipes()
supplies = ins.Insumos()
maximo = 0
menor = 0
num_generaciones = 20
tam_torneo = 2
promedios = []
mejores = []
menores = []

# Población de prueba a 10
population_test = [
    [5, 7, 8, 8, 7, 7, 2, 5, 7, 6, 1, 5, 2, 4, 7, 7, 0, 2, 9],
    [3, 0, 0, 7, 4, 9, 5, 0, 3, 9, 5, 7, 3, 2, 0, 4, 4, 1, 2],
    [1, 5, 8, 9, 8, 0, 3, 1, 8, 4, 9, 5, 0, 5, 9, 1, 1, 2, 2],
    [0, 4, 7, 1, 7, 1, 5, 9, 2, 5, 6, 1, 6, 3, 8, 5, 5, 3, 2],
    [4, 8, 3, 5, 6, 5, 5, 7, 6, 2, 4, 2, 7, 5, 4, 1, 8, 8, 2],
    [6, 9, 4, 9, 7, 6, 0, 2, 5, 3, 6, 4, 4, 8, 3, 6, 4, 4, 7],
    [2, 0, 0, 9, 9, 6, 1, 9, 0, 9, 0, 9, 6, 1, 4, 3, 3, 1, 0],
    [3, 3, 6, 0, 4, 9, 4, 5, 7, 3, 0, 0, 4, 2, 6, 0, 8, 3, 1],
    [4, 3, 6, 2, 7, 6, 8, 8, 7, 2, 4, 5, 0, 8, 0, 3, 6, 7, 4]
]
population = np.array(population_test)
# population = np.array(0, 10, size=(num_persons, num_recipes))
# Mutación entre 0 a 10, se muta, en un número aleatorio de 0 a 1000, y es gen por gen

def funcion_aptitud(individuo):
    ganancias = 0
    merma = 0
    tiempo_total = 0
    tiempo_limite = 3 * 240
    insumos_usados = {}

    for i, (nombre_receta, cantidad) in enumerate(zip(recipes.recipes.keys(), individuo)):
        precio_receta = recipes.obtener_recipes(nombre_receta)['Precio']
        tiempo_receta = recipes.obtener_recipes(nombre_receta)['Tiempo elaboración']

        if tiempo_total + cantidad * tiempo_receta > tiempo_limite:
            cantidad = (tiempo_limite - tiempo_total) // tiempo_receta

        ganancias += cantidad * precio_receta
        tiempo_total += cantidad * tiempo_receta

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

    aptitud = merma - ganancias
    return aptitud


def seleccion_torneo(poblacion, funcion_aptitud, tam_torneo=3):
    seleccionados = random.sample(poblacion, tam_torneo)
    aptitudes = [funcion_aptitud(individuo) for individuo in seleccionados]
    indice_ganador = aptitudes.index(min(aptitudes))
    return seleccionados[indice_ganador]


def cruce(padre1, padre2):
    hijo1 = np.zeros_like(padre1)
    hijo2 = np.zeros_like(padre2)

    for i in range(len(padre1)):
        if np.random.rand() < 0.5:
            hijo1[i] = padre1[i]
            hijo2[i] = padre2[i]
        else:
            hijo1[i] = padre2[i]
            hijo2[i] = padre1[i]

    probabilidad = np.random.randint(0, 100)
    if 0 < probabilidad <= 90:
        return hijo1, hijo2
    else:
        return padre1, padre2

def mutacion(individuo):
    for i in range(len(individuo)):
        probabilidad_mutacion = np.random.randint(0, 1001)
        if probabilidad_mutacion <= 10:
            individuo[i] = np.random.randint(0, 10)

    return individuo


for generacion in range(num_generaciones):
    print(f'Generación {generacion + 1}')

    aptitudes = [funcion_aptitud(individuo) for individuo in population_test]

    promedio = sum(aptitudes) / len(aptitudes)
    mejor = max(aptitudes)
    menor = min(aptitudes)

    promedios.append(promedio)
    mejores.append(mejor)
    menores.append(menor)

    print(f'Promedio de aptitud: {promedio:.2f}')
    print(f'Mejor aptitud: {mejor:.2f}')
    print(f'Peor aptitud: {menor:.2f}')

    nueva_poblacion = []
    for _ in range(num_persons // 2):
        padre1 = seleccion_torneo(population_test, funcion_aptitud, tam_torneo)
        padre2 = seleccion_torneo(population_test, funcion_aptitud, tam_torneo)

        hijo1, hijo2 = cruce(padre1, padre2)

        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)

        nueva_poblacion.extend([hijo1, hijo2])
    population_test = nueva_poblacion

plt.plot(promedios, label='Promedio')
plt.plot(menores, label='Mejores')
plt.plot(mejores, label='Peores')
plt.xlabel('Generación')
plt.ylabel('Aptitud')
plt.legend()
plt.show()
