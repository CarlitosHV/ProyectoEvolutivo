class Recipes:
    def __init__(self):
        self.recipes = {
            "Frappé Mocha": {
                "Leche": 0.250,
                "Hielo": 0.50,
                "Saborizante Mocha": 0.25,
                "Crema Batida": 0.10,
                "Chocolate líquido": 0.10,
                "Precio": 59,
                "Costo elaboración": 51.78,
                "Tiempo elaboración": 5
            },
            "Frappé Chocolate Blanco": {
                "Leche": 0.250,
                "Hielo": 100,
                "Saborizante Chocolate Blanco": 0.25,
                "Base láctea": 0.10,
                "Crema Batida": 0.10,
                "Chocolate líquido": 0.10,
                "Precio": 59,
                "Costo elaboración": 52.47,
                "Tiempo elaboración": 5
            },
            "Frappé Taro": {
                "Leche": 0.250,
                "Hielo": 0.100,
                "Saborizante Taro": 0.25,
                "Crema Batida": 0.10,
                "Chocolate líquido": 0.10,
                "Precio": 59,
                "Costo elaboración": 52.47,
                "Tiempo elaboración": 5
            },
            "Frappé Oreo": {
                "Leche": 0.250,
                "Hielo": 0.100,
                "Saborizante Chocolate Blanco": 0.25,
                "Galletas Oreo": 2,
                "Base láctea": 0.10,
                "Crema Batida": 0.10,
                "Chocolate líquido": 0.10,
                "Precio": 62,
                "Costo elaboración": 55.19,
                "Tiempo elaboración": 5
            },
            "Frappé Carlos V": {
                "Leche": 0.250,
                "Hielo": 0.100,
                "Saborizante Chocolate": 0.25,
                "Chocolates": 2,
                "Crema Batida": 0.10,
                "Chocolate líquido": 0.10,
                "Precio": 62,
                "Costo elaboración": 55.19,
                "Tiempo elaboración": 5
            },
            "Frappé Chocolate": {
                "Leche": 0.250,
                "Hielo": 0.100,
                "Saborizante Chocolate": 0.25,
                "Crema Batida": 0.10,
                "Chocolate líquido": 0.10,
                "Precio": 59,
                "Costo elaboración": 52.47,
                "Tiempo elaboración": 5
            },
            "Soda Italiana Mora Azul": {
                "Hielo": 0.100,
                "Agua Mineral": 0.200,
                "Jarabe Mora Azul": 0.10,
                "Precio": 35,
                "Costo elaboración": 9.45,
                "Tiempo elaboración": 2
            },
            "Soda Italiana Cereza": {
                "Hielo": 0.100,
                "Agua Mineral": 0.200,
                "Jarabe Cereza": 0.10,
                "Precio": 45,
                "Costo elaboración": 9.45,
                "Tiempo elaboración": 2
            },
            "Soda Italiana Lima": {
                "Hielo": 0.100,
                "Agua Mineral": 200,
                "Jarabe Lima": 10,
                "Precio": 45,
                "Costo elaboración": 9.45,
                "Tiempo elaboración": 2
            },
            "Malteada Fresa": {
                "Helado Fresa": 0.050,
                "Leche": 0.250,
                "Azúcar": 0.10,
                "Chocolate líquido": 10,
                "Precio": 52,
                "Costo elaboración": 19.61,
                "Tiempo elaboración": 4
            },
            "Malteada Vainilla": {
                "Helado Vainilla": 0.050,
                "Leche": 0.250,
                "Azúcar": 0.10,
                "Chocolate líquido": 10,
                "Precio": 52,
                "Costo elaboración": 19.61,
                "Tiempo elaboración": 4
            },
            "Malteada Chocolate": {
                "Helado Chocolate": 0.050,
                "Leche": 0.250,
                "Azúcar": 0.10,
                "Chocolate líquido": 10,
                "Precio": 52,
                "Costo elaboración": 19.61,
                "Tiempo elaboración": 4
            },
            "Malteada Carlos V": {
                "Helado Chocolate": 50,
                "Leche": 0.250,
                "Azúcar": 10,
                "Chocolates": 2,
                "Chocolate líquido": 10,
                "Precio": 59,
                "Costo elaboración": 22.82,
                "Tiempo elaboración": 4
            },
            "Malteada Oreo": {
                "Helado Chocolate": 50,
                "Leche": 0.250,
                "Azúcar": 0.10,
                "Galletas Oreo": 2,
                "Chocolate líquido": 10,
                "Precio": 59,
                "Costo elaboración": 22.82,
                "Tiempo elaboración": 4
            },
            "Capuccino": {
                "Café Expresso": 0.16,
                "Agua": 0.70,
                "Leche": 0.50,
                "Precio": 35,
                "Costo elaboración": 15.29,
                "Tiempo elaboración": 5
            },
            "Capuccino Amaretto": {
                "Café Expresso": 0.16,
                "Agua": 0.70,
                "Leche": 0.50,
                "Jarabe Amaretto": 0.25,
                "Precio": 39,
                "Costo elaboración": 17.17,
                "Tiempo elaboración": 5
            },
            "Capuccino Cajeta": {
                "Café Expresso": 0.16,
                "Agua": 0.70,
                "Leche": 0.50,
                "Jarabe Cajeta": 0.25,
                "Precio": 39,
                "Costo elaboración": 17.17,
                "Tiempo elaboración": 5
            },
            "Capuccino Menta Francesa": {
                "Café Expresso": 0.16,
                "Agua": 0.70,
                "Leche": 0.50,
                "Jarabe Menta Francesa": 0.25,
                "Precio": 39,
                "Costo elaboración": 17.17,
                "Tiempo elaboración": 5
            }
        }

    def obtener_recipes(self, nombre):
        if nombre in self.recipes:
            return self.recipes[nombre]
        else:
            return None
