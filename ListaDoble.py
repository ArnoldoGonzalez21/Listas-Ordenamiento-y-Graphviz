#from typing import final
from Robot import Robot
from Posicion import Posicion
from Terreno import Terreno

class ListaDoble():
    
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0
        self.inicio_terreno = None
        self.final_terreno = None
        self.size_terreno = 0
                
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
    
    def insertar_terrenos(self, indice, nombre, dim_x, dim_y): 
        nuevo_terreno = Terreno(indice, nombre, dim_x, dim_y)
        self.size_terreno += 1
        if self.inicio_terreno is None:
            self.inicio_terreno = nuevo_terreno
            self.final_terreno = nuevo_terreno
        else:
            tmp = self.inicio_terreno
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo_terreno
            nuevo_terreno.anterior = tmp
            self.final_terreno = nuevo_terreno        

    def showTerr(self):
        actual = self.inicio_terreno
        while actual is not None:
            temp = actual.siguiente
            if temp is None:
                print(actual.nombre)  
                break
            print(actual.nombre)  
            actual = actual.siguiente
           


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
        final = self.final
        while actual is not None:
            derecha = object 
            izquierda = object 
            abajo = object 
            arriba = object
            valor_derecha = False 
            valor_izquierda = False
            valor_abajo = False
            valor_arriba = False
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
                    valor_abajo = True
                    break
                s = s.siguiente
            
            while d is not None:
                tmp = d.siguiente
                if tmp is None:
                    break
                if int(tmp.x) == int(actual.x) and int(tmp.y) == int(actual.y)+1:
                    derecha = tmp 
                    valor_derecha = True 
                    print("Derecha valor: ",derecha.valor)                
                    break
                d = d.siguiente
            
            while w is not None:
                tmp = w.siguiente
                if tmp is None:
                    break
                if  int(actual.x) - 1 == 1 and int(actual.y) == 1:
                    arriba = w  
                    valor_arriba = True           
                    print("Arriba valor: ",arriba.valor)
                    break
                if int(tmp.x) == int(actual.x) - 1 and int(tmp.y) == int(actual.y):
                    arriba = tmp 
                    valor_arriba = True             
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
                    valor_izquierda = True
                    print('Izquierda valor: ',izquierda.valor)
                    break
                a = a.siguiente  
            
            posiciones = []
            if valor_abajo is True:
                nuevo = Robot(abajo, abajo.valor)
                posiciones.insert(len(posiciones),nuevo)
            if valor_derecha is True:
                nuevo = Robot(derecha, derecha.valor)
                posiciones.insert(len(posiciones),nuevo)
            if valor_izquierda is True:
                nuevo = Robot(izquierda, izquierda.valor)
                posiciones.insert(len(posiciones),nuevo)
            if valor_arriba is True:
                nuevo = Robot(arriba, arriba.valor)
                posiciones.insert(len(posiciones),nuevo)
            
            for i in range(1,len(posiciones)):
                for j in range(0,len(posiciones)-i):
                    if (posiciones[j+1].valor > posiciones[j].valor):
                        aux = posiciones[j].valor
                        posiciones[j].valor = posiciones[j+1].valor
                        posiciones[j+1].valor = aux                
            print('\n------------------\n')
            for s in posiciones:
                print(s.valor)   
            temporal = actual
            elegido = object
            
            while j <= len(posiciones):                
                if actual is not actual.anterior: 
                    elegido = posiciones[j].posicion 
                    j = len(posiciones)
                    break
                j += 1                     
                
            #for i in range(0,len(posiciones)): 
             #   if actual is not actual.anterior: 
              #      elegido = posiciones[i].posicion  
               #     break
                       
            print("elegido:",elegido.valor)           
            posiciones.clear()     
            actual = elegido
            #actual = actual.siguiente
            if elegido == final:
                break
            
            
            