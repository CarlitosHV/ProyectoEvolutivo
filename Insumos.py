class Insumos:
    def __init__(self):
        self.insumos = {
            "Leche": {
                "Cantidad": 24,
                "Precio": 270
            },
            "Hielo": {
                "Cantidad": 10,
                "Precio": 29
            },
            "Base láctea": {
                "Cantidad": 2,
                "Precio": 280
            },
            "Galletas Oreo": {
                "Cantidad": 30,
                "Precio": 50
            },
            "Chocolates": {
                "Cantidad": 20,
                "Precio": 40
            },
            "Agua Mineral": {
                "Cantidad": 7,
                "Precio": 46
            },
            "Café Expresso": {
                "Cantidad": 4,
                "Precio": 768
            },
            "Agua": {
                "Cantidad": 40,
                "Precio": 47
            },
            "Jarabe Lima": {
                "Cantidad": 2,
                "Precio": 217
            },
            "Jarabe Cereza": {
                "Cantidad": 2,
                "Precio": 217
            },
            "Jarabe Mora Azul": {
                "Cantidad": 2,
                "Precio": 217
            },
            "Jarabe Menta Francesa": {
                "Cantidad": 2,
                "Precio": 217
            },
            "Jarabe Amaretto": {
                "Cantidad": 2,
                "Precio": 217
            },
            "Jarabe Cajeta": {
                "Cantidad": 2,
                "Precio": 217
            },
            "Saborizante Mocha": {
                "Cantidad": 2,
                "Precio": 273
            },
            "Saborizante Chocolate Blanco": {
                "Cantidad": 2,
                "Precio": 273
            },
            "Saborizante Taro": {
                "Cantidad": 2,
                "Precio": 273
            },
            "Saborizante Chocolate": {
                "Cantidad": 2,
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

    def obtener_insumo(self, nombre):
        if nombre in self.insumos:
            return self.insumos[nombre]
        else:
            return None

    def agregar_insumo(self, nombre, cantidad, Precio_Precio):
        if nombre in self.insumos:
            self.insumos[nombre]["Cantidad"] += cantidad
            self.insumos[nombre]["Precio/Precio"] = Precio_Precio
        else:
            self.insumos[nombre] = {"Cantidad": cantidad, "Precio/Precio": Precio_Precio}

    def mostrar_insumos(self):
        for nombre, detalles in self.insumos.items():
            print(f"{nombre}: Cantidad - {detalles['Cantidad']}, Precio/Precio - {detalles['Precio/Precio']}")
