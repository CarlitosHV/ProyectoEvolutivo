import numpy as np
import Insumos as ins
import Recipes as rec

# Mi configuración del individuo e instancias
num_recipes = 19
num_persons = 20
recipes = rec.Recipes()
supplies = ins.Insumos()

def funcion_aptitud(individuo):
    ganancias = 0
    merma = 0
    tiempo_total = 0

    # Calculo las ganancias y el tiempo total
    for i, (nombre_receta, cantidad) in enumerate(zip(recipes.recipes.keys(), individuo)):
        ganancias += cantidad * recipes.obtener_recipes(nombre_receta)['Precio']
        tiempo_total += cantidad * recipes.obtener_recipes(nombre_receta)['Tiempo elaboración']

    # Si el tiempo total excede el límite, penalizamos la aptitud
    if tiempo_total / 3 > 210:
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


    # La aptitud es igual a las ganancias menos la merma
    aptitud = merma - ganancias

    return aptitud



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

# Calcular la aptitud de cada individuo en la población de prueba
aptitudes = []
for i, individuo in enumerate(population_test):
    fitness = funcion_aptitud(individuo)
    aptitudes.append(fitness)
    print(f'La aptitud del individuo {i + 1} es: {fitness:.2f}')

# Calcular el promedio de aptitud
promedio_aptitud = sum(aptitudes) / len(aptitudes)
print(f'El promedio de aptitud para esta generación es: {  promedio_aptitud:.2f}')




'''# Aquí utilizo por torneo
def seleccion(poblacion, aptitudes, tamano_torneo):
    # Crear un nuevo array para almacenar los individuos seleccionados
    seleccionados = np.empty_like(poblacion)

    # Para cada lugar en los seleccionados
    for i in range(poblacion.shape[0]):
        # Elegir individuos aleatorios para el torneo
        competidores_idx = np.random.randint(0, poblacion.shape[0], size=tamano_torneo)
        competidores_aptitudes = aptitudes[competidores_idx]

        # Encontrar el mejor individuo del torneo
        ganador_idx = competidores_idx[np.argmax(competidores_aptitudes)]

        # Añadir el ganador a los seleccionados
        seleccionados[i] = poblacion[ganador_idx]

    return seleccionados


# Utilizo la cruza en varios puntos
def cruza(padre1, padre2, num_puntos):
    # Genero los puntos de cruza
    puntos = np.sort(np.random.choice(range(1, len(padre1)), size=num_puntos, replace=False))

    # Inicializo los hijos
    hijo1, hijo2 = padre1.copy(), padre2.copy()

    # Realizo la cruza
    for i in range(num_puntos):
        if i % 2 == 0:
            # Obtengo los 2 hijos
            hijo1[puntos[i]:puntos[i+1]] = padre2[puntos[i]:puntos[i+1]]
            hijo2[puntos[i]:puntos[i+1]] = padre1[puntos[i]:puntos[i+1]]

    return hijo1, hijo2
'''
