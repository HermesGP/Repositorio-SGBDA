from datetime import datetime
class animal:
    def __init__(self, id, especie):
        self.id = id
        self.especie = especie
    def __str__(self):
        return f"ID: {self.id}, Especie: {self.especie}"
class vacuno(animal):
    #El carimbo de un animal es la última cifra del año posterior a su nacimiento
    #Los animales son de origen criollo por defecto, es decir, nacidos en la granja
    #El peso es opcional y por defecto es desconocido
    def __init__(self, id, especie, raza, carimbo, origen="Criollo", peso="desconocido"):
        super().__init__(id, especie)
        self.raza = raza
        self.especie = "Vacuno"
        self.carimbo = carimbo
        self.origen = origen
        self.peso = peso
        # Almacena la fecha de carga del animal con el formato YYYY-MM-DD
        # datetime.now() obtiene la fecha y hora actuales
        self.fecha_carga = datetime.now()
    def venta(self, precio):
        self.precio = precio
        self.fecha_venta = datetime.now()
        return self.precio, self.fecha_venta
class ovino(animal):
    #Para los ovinos la raza y el carimbo son irrelevantes
    def __init__(self, id, especie, origen, peso="desconocido"):
        super().__init__(id, especie)
        self.especie = "Ovino"
        self.origen = origen
        self.peso = peso
        self.fecha_carga = datetime.now()
    def venta(self, venta):
        self.precio = venta.precio
        self.fecha_venta = datetime.now()
        return self.precio, self.fecha_venta
