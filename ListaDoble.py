from Robot import Robot
from Posicion import Posicion

class ListaDoble():
    
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0
                
    def insertar(self, x, y,valor): 
        nueva_posicion = Posicion(x, y,valor)
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

    def showPos(self):
        actual = self.inicio
        while actual is not None:
            temp = actual.siguiente
            if temp is None:
                print(actual.valor + '\t', end = " ") 
                break
            if actual.x < temp.x:
                print(actual.valor + '\t')  
            else:
                print(actual.valor + '\t', end = " ")
            actual = actual.siguiente
            
    def verRuta(self):
        actual = self.inicio
        while actual is not None:
            derecha = object 
            izquierda = object 
            abajo = object 
            arriba = object
            a = actual 
            s = actual 
            d = actual
            w = self.inicio            
            print('\n...............')
            print("Actual valor: ",actual.valor)            
            while s is not None:
                tmp = s.siguiente
                if tmp is None:
                    break
                if int(tmp.x) == int(actual.x)+1 and int(tmp.y) == int(actual.y):
                    abajo = tmp                   
                    print("Abajo valor: ",abajo.valor)
                    break
                s = s.siguiente
            while d is not None:
                tmp = d.siguiente
                if tmp is None:
                    break
                if int(tmp.x) == int(actual.x) and int(tmp.y) == int(actual.y)+1:
                    derecha = tmp    
                    print("Derecha valor: ",derecha.valor)                
                    break
                d = d.siguiente
            while w is not None:
                tmp = w.siguiente
                if tmp is None:
                    break
                ##if int(w.x) == 1:
                  #  w = w.siguiente
                   # continue
                #print(int(tmp.x), int(actual.x) - 1 ,int(tmp.y) ,int(actual.y))
                if  int(actual.x) - 1 == 1 and int(actual.y) == 1:
                    arriba = w              
                    print("Arriba valor: ",arriba.valor)
                    break
                if int(tmp.x) == int(actual.x) - 1 and int(tmp.y) == int(actual.y):
                    arriba = tmp              
                    print("Arriba valor: ",arriba.valor)
                    break
                w = w.siguiente
            while a is not None:
                tmp = a.anterior
                if tmp is None:
                    break
                if int(a.x) == 1 and int(a.y) == 1:
                    a = a.siguiente 
                if int(tmp.x) == int(actual.x) and int(tmp.y) == int(actual.y)-1:
                    izquierda = tmp
                    print('Izquierda valor: ',izquierda.valor)
                    break
                a = a.siguiente       
            actual = actual.siguiente