class Posicion():
    def __init__(self, indice_terreno, id, x, y, valor):
        self.indice_terreno = indice_terreno
        self.id = id
        self.x = x
        self.y = y
        self.valor = valor
        self.siguiente = None
        self.anterior = None
        