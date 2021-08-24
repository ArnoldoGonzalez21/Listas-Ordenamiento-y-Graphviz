class Robot():
    def __init__(self, posicion,valor, nombre):
        self.posicion = posicion
        self.nombre = nombre
        self.valor = valor
        self.inicio = None
        self.final = None
        self.size = 0
        self.siguiente = None
        self.anterior = None 
    
    def insertar_Robot(self, posicion,valor, nombre): 
        nueva_posicion = Robot(posicion,valor, nombre)
        self.size += 1
        if self.inicio is None:
            self.inicio = nueva_posicion
            self.final = nueva_posicion
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nueva_posicion
            nueva_posicion.anterior = tmp
            self.final = nueva_posicion
    