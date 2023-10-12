import numpy as np

# Mis insumos
Insumos = {
    "Leche": {
        "Cantidad": 12,
        "Costo": 270
    },
    "Hielo": {
        "Cantidad": 5,
        "Costo": 29
    },
    "Base láctea": {
        "Cantidad": 1,
        "Precio": 280
    },
    "Galleta Oreo": {
        "Cantidad": 20,
        "Precio": 50
    },
    "Chocolates": {
        "Cantidad": 20,
        "Precio": 40
    },
    "Agua Mineral": {
        "Cantidad": 3.5,
        "Precio": 46
    },
    "Café Expresso": {
        "Cantidad": 2,
        "Precio": 768
    },
    "Agua": {
        "Cantidad": 18,
        "Precio": 47
    },
    "Jarabe Lima": {
        "Cantidad": 1,
        "Precio": 217
    },
    "Jarabe Cereza": {
        "Cantidad": 1,
        "Precio": 217
    },
    "Jarabe Mora Azul": {
        "Cantidad": 1,
        "Precio": 217
    },
    "Jarabe Menta Francesa": {
        "Cantidad": 1,
        "Precio": 217
    },
    "Jarabe Amaretto": {
        "Cantidad": 1,
        "Precio": 217
    },
    "Jarabe Cajeta": {
        "Cantidad": 1,
        "Precio": 217
    },
    "Saborizante Mocha": {
        "Cantidad": 1,
        "Precio": 273
    },
    "Saborizante Chocolate Blanco": {
        "Cantidad": 1,
        "Precio": 273
    },
    "Saborizante Taro": {
        "Cantidad": 1,
        "Precio": 273
    },
    "Saborizante Chocolate": {
        "Cantidad": 1,
        "Precio": 273
    },
    "Helado Fresa": {
        "Cantidad": 3,
        "Precio": 189
    },
    "Helado Vainilla": {
        "Cantidad": 3,
        "Precio": 189
    },
    "Helado Chocolate": {
        "Cantidad": 3,
        "Precio": 189
    },
    "Crema Batida": {
        "Cantidad": 184,
        "Precio": 95
    },
    "Chocolate líquido": {
        "Cantidad": 589,
        "Precio": 68
    },
    "Azúcar": {
        "Cantidad": 3,
        "Precio": 89
    }
}
# Mis recetas, son 19 actualmente
Recetas = {
    "Frappé Mocha": {
        "Leche": 250,
        "Hielo": 50,
        "Saborizante Mocha": 25,
        "Crema Batida": 10,
        "Chocolate Líquido": 10,
        "Precio": 59,
        "Costo elaboración": 51.78,
        "Tiempo elaboración": 5
    },
    "Frappé Chocolate Blanco": {
        "Leche": 250,
        "Hielo": 100,
        "Saborizante Chocolate Blanco": 25,
        "Base Láctea": 10,
        "Crema Batida": 10,
        "Chocolate Líquido": 10,
        "Precio": 59,
        "Costo elaboración": 52.47,
        "Tiempo elaboración": 5
    },
    "Frappé Taro": {
        "Leche": 250,
        "Hielo": 100,
        "Saborizante Taro": 25,
        "Crema Batida": 10,
        "Chocolate Líquido": 10,
        "Precio": 59,
        "Costo elaboración": 52.47,
        "Tiempo elaboración": 5
    },
    "Frappé Oreo": {
        "Leche": 250,
        "Hielo": 100,
        "Saborizante Chocolate Blanco": 25,
        "Galleta Oreo": 2,
        "Base láctea": 10,
        "Crema Batida": 10,
        "Chocolate Líquido": 10,
        "Precio": 62,
        "Costo elaboración": 55.19,
        "Tiempo elaboración": 5
    },
    "Frappé Carlos V": {
        "Leche": 250,
        "Hielo": 100,
        "Saborizante Chocolate": 25,
        "Chocolates": 2,
        "Crema Batida": 10,
        "Chocolate Líquido": 10,
        "Precio": 62,
        "Costo elaboración": 55.19,
        "Tiempo elaboración": 5
    },
    "Frappé Chocolate": {
        "Leche": 250,
        "Hielo": 100,
        "Saborizante Chocolate": 25,
        "Crema Batida": 10,
        "Chocolate Líquido": 10,
        "Precio": 59,
        "Costo elaboración": 52.47,
        "Tiempo elaboración": 5
    },
    "Soda Italiana Mora Azul": {
        "Hielo": 100,
        "Agua Mineral": 200,
        "Jarabe Mora Azul": 10,
        "Precio": 35,
        "Costo elaboración": 9.45,
        "Tiempo elaboración": 2
    },
    "Soda Italiana Cereza": {
        "Hielo": 100,
        "Agua Mineral": 200,
        "Jarabe Cereza": 10,
        "Precio": 45,
        "Costo elaboración": 9.45,
        "Tiempo elaboración": 2
    },
    "Soda Italiana Lima": {
        "Hielo": 100,
        "Agua Mineral": 200,
        "Jarabe Lima": 10,
        "Precio": 45,
        "Costo elaboración": 9.45,
        "Tiempo elaboración": 2
    },
    "Malteada Fresa": {
        "Helado Fresa": 50,
        "Leche": 250,
        "Azúcar": 10,
        "Chocolate líquido": 10,
        "Precio": 52,
        "Costo elaboración": 19.61,
        "Tiempo elaboración": 4
    },
    "Malteada Vainilla": {
        "Helado Vainilla": 50,
        "Leche": 250,
        "Azúcar": 10,
        "Chocolate líquido": 10,
        "Precio": 52,
        "Costo elaboración": 19.61,
        "Tiempo elaboración": 4
    },
    "Malteada Chocolate": {
        "Helado Chocolate": 50,
        "Leche": 250,
        "Azúcar": 10,
        "Chocolate líquido": 10,
        "Precio": 52,
        "Costo elaboración": 19.61,
        "Tiempo elaboración": 4
    },
    "Malteada Carlos V": {
        "Helado Chocolate": 50,
        "Leche": 250,
        "Azúcar": 10,
        "Chocolate": 2,
        "Chocolate líquido": 10,
        "Precio": 59,
        "Costo elaboración": 22.82,
        "Tiempo elaboración": 4
    },
    "Malteada Oreo": {
        "Helado Chocolate": 50,
        "Leche": 250,
        "Azúcar": 10,
        "Galletas Oreo": 2,
        "Chocolate líquido": 10,
        "Precio": 59,
        "Costo elaboración": 22.82,
        "Tiempo elaboración": 4
    },
    "Capuccino": {
        "Café Expresso": 16,
        "Agua": 70,
        "Leche": 50,
        "Precio": 35,
        "Costo elaboración": 15.29,
        "Tiempo elaboración": 5
    },
    "Capuccino Amaretto": {
        "Café Expresso": 16,
        "Agua": 70,
        "Leche": 50,
        "Jarabe Amaretto": 25,
        "Precio": 39,
        "Costo elaboración": 17.17,
        "Tiempo elaboración": 5
    },
    "Capuccino Cajeta": {
        "Café Expresso": 16,
        "Agua": 70,
        "Leche": 50,
        "Jarabe Cajeta": 25,
        "Precio": 39,
        "Costo elaboración": 17.17,
        "Tiempo elaboración": 5
    },
    "Capuccino Menta Francesa": {
        "Café Expresso": 16,
        "Agua": 70,
        "Leche": 50,
        "Jarabe Menta Francesa": 25,
        "Precio": 39,
        "Costo elaboración": 17.17,
        "Tiempo elaboración": 5
    }
}

# Mi configuración del individuo
num_recetas = 19
num_individuos = 100

poblacion = np.random.randint(0, 10, size=(num_individuos, num_recetas))


def funcion_aptitud(individuo, recetas, insumos):
    ganancias = 0
    merma = 0

    # Calculo las ganancias
    for i, cantidad in enumerate(individuo):
        ganancias += cantidad * recetas[i]['Precio']

    # Calculo la merma
    insumos_usados = {}
    for i, cantidad in enumerate(individuo):
        for insumo, cantidad_insumo in recetas[i].items():
            if insumo not in insumos_usados:
                insumos_usados[insumo] = 0
            insumos_usados[insumo] += cantidad * cantidad_insumo
    for insumo, cantidad in insumos_usados.items():
        if cantidad > insumos[insumo]['Cantidad']:
            merma += (cantidad - insumos[insumo]['Cantidad']) * insumos[insumo]['Costo']

    # La aptitud es igual a las ganancias menos la merma
    aptitud = ganancias - merma

    return aptitud

# Aquí utilizo por torneo
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

def mutacion(individuo, prob_mutacion):
    for i in range(len(individuo)):
        if np.random.random() < prob_mutacion:
            individuo[i] += np.random.randint(-2, 3)  # Agrego un número aleatorio entre -2 y 2
            individuo[i] = max(0, individuo[i])  # Aseguro que el número de recetas no sea negativo
    return individuo



