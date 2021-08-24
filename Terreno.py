class Terreno():
    def __init__(self, indice, nombre, dimension_x, dimension_y, inicio_x, inicio_y, final_x, final_y):
        self.indice = indice
        self.nombre = nombre
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y  
        self.incio_x = inicio_x
        self.incio_y = inicio_y
        self.final_x = final_x
        self.final_y = final_y      
        self.siguiente = None
        self.anterior = None