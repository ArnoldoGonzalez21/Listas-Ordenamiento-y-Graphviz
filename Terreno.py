class Terreno():
    def __init__(self, indice, nombre, dimension_x, dimension_y):
        self.indice = indice
        self.nombre = nombre
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y        
        self.siguiente = None
        self.anterior = None