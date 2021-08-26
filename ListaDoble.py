#from typing import final
from Robot import Robot
from Posicion import Posicion
from Terreno import Terreno

inicio_x = 0    
inicio_y = 0
fin_x = 0
fin_y = 0
dim_x = 0
dim_y = 0  
combustible = 9999
class ListaDoble():
  
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0
        self.inicio_terreno = None
        self.final_terreno = None
        self.size_terreno = 0
                
    def insertar(self, indice_terreno, id, x, y, valor, entro): 
        nueva_posicion = Posicion(indice_terreno, id, x, y, valor, entro)
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
    
    def insertar_terrenos(self, indice, nombre, dim_x, dim_y, ini_x, ini_y, fin_x, fin_y): 
        nuevo_terreno = Terreno(indice, nombre, dim_x, dim_y, ini_x, ini_y, fin_x, fin_y)
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

    def mostrar_posiciones(self, indice_terreno):
        actual = self.inicio
        while actual is not None:
            if actual.indice_terreno is indice_terreno:
                tmp = actual.siguiente
                if tmp is None:
                    print(actual.valor, '\t', end = " ") 
                    break
                if actual.x < tmp.x:
                    print(actual.valor, '\t')  
                else:
                    print(actual.valor, '\t', end = " ")
                actual = actual.siguiente 
            else:
                actual = actual.siguiente 
        
    def mostrar_posiciones_camino(self, indice_terreno):
        actual = self.inicio
        while actual is not None:
            if actual.indice_terreno is indice_terreno:
                tmp = actual.siguiente
                if tmp is None:
                    if actual.entro is True: print('1','\t', end = " ")
                    else: print('O','\t', end = " ")
                    break
                if actual.x < tmp.x:
                    if actual.entro is True: print('1','\t')
                    else: print('O','\t')
                else:
                    if actual.entro is True: print('1','\t', end = " ")
                    else: print('O','\t', end = " ")
                actual = actual.siguiente 
            else:
                actual = actual.siguiente  
        print('\n')                   
        
    def buscar_terreno(self,nombre_terreno):
        actual_ter = self.inicio_terreno
        while actual_ter is not None:
            if nombre_terreno == actual_ter.nombre:
                return actual_ter.indice  
            actual_ter = actual_ter.siguiente  
             
    def buscar_nombre_terreno(self,indice_terreno):
        actual_ter = self.inicio_terreno
        while actual_ter is not None:
            if indice_terreno is actual_ter.indice:
                return actual_ter.nombre  
            actual_ter = actual_ter.siguiente
        return 'Nombre Desconocido'              
     
    def datos_terreno(self, indice_terreno):
        global inicio_x 
        global inicio_y 
        global fin_x 
        global fin_y
        global dim_x
        global dim_y
        actual_datos = self.inicio_terreno
        while actual_datos is not None:
            if actual_datos.indice is indice_terreno:
                inicio_x = actual_datos.incio_x
                inicio_y = actual_datos.incio_y
                fin_x = actual_datos.final_x
                fin_y = actual_datos.final_y
                dim_x = actual_datos.dimension_x
                dim_y = actual_datos.dimension_y
                break
            actual_datos = actual_datos.siguiente
    
    def contenido_lateral(self):
        global dim_y
        global dim_x
        contenido = ''
        contenido_fila_columna = ''
        contenido_enlace = ''
        rango_fila = int(dim_x)
        rango_columna = int(dim_y)
        for i in range(rango_fila):
            contenido_fila_columna += 'F'+str(i+1)+'[label=\"'+str(i+1)+'\",group=1,fillcolor=yellow];\n'
        for j in range(rango_columna):
            contenido_fila_columna += 'C'+str(j+1)+'[label=\"'+str(j+1)+'\",group='+str(j+2)+',fillcolor=yellow];\n'
        for k in range(rango_fila - 1):
            contenido_enlace += 'F'+str(k+1)+' -> F'+str(k+2)+';\n'
        for m in range(rango_columna - 1):
            contenido_enlace += 'C'+str(m+1)+' -> C'+str(m+2)+';\n'        
        contenido = contenido_fila_columna + contenido_enlace
        contenido += 'raiz -> F1; \nraiz -> C1;\n{rank = same;raiz;'
        for n in range(rango_columna):
            contenido += 'C'+str(n+1)
            if n < rango_columna - 1:
                contenido += ';'      
        contenido += '}'
        print(contenido)
        return contenido
    
    def enlazar_nodos(self, indice_terreno, termino):
        global dim_y
        global dim_x
        contenido = ''
        contenido_enlace_c = ''
        contenido_enlace_f = ''
        contenido_enlace_nodo_f = ''
        contenido_enlace_nodo_c = ''
        contenido_enlace_rank = ''
        i = 0
        j = 0
        k = 0
        actual = self.inicio
        actual_enlace = self.inicio
        actual_enlace_2 = self.inicio
        while actual is not None:
            if actual.indice_terreno is indice_terreno:
                tmp = actual.siguiente
                if tmp is None:
                    break
                if termino:
                    if actual.entro: 
                        contenido += 'nodo'+actual.x+'_'+actual.y+'[label=\"1\",fillcolor=green,group='+str(int(actual.y) + 1)+']\n'
                    else:
                        contenido += 'nodo'+actual.x+'_'+actual.y+'[label=\"O\",fillcolor=gray,group='+str(int(actual.y) + 1)+']\n'
                else: 
                    contenido += 'nodo'+actual.x+'_'+actual.y+'[label=\"'+actual.valor+'\",fillcolor=green,group='+str(int(actual.y) + 1)+']\n'
                if actual.x == str(1):
                    contenido_enlace_c += 'C'+str(i+1)+' -> nodo'+actual.x+'_'+actual.y+';\n'
                    i += 1
                if actual.y == str(1):
                    contenido_enlace_f += 'F'+str(j+1)+' -> nodo'+actual.x+'_'+actual.y+';\n'
                    j += 1
                if actual.y < tmp.y:   
                    contenido_enlace_nodo_f += 'nodo'+actual.x+'_'+actual.y+' -> nodo'+tmp.x+'_'+tmp.y+';\n'      
                actual = actual.siguiente
            else:
                actual = actual.siguiente
         
        rango_fila = int(dim_x)
        for i in range(rango_fila):
            contenido_enlace_rank += '{rank = same;F'+str(i+1)      
            while actual_enlace is not None:
                if actual_enlace.indice_terreno is indice_terreno:
                    tmp = actual_enlace.siguiente
                    if tmp is None:
                        break
                    if actual_enlace.x == str(i+1):
                        contenido_enlace_rank += ';nodo'+actual_enlace.x+'_'+actual_enlace.y+''
                    else:
                        break
                    
                    actual_enlace = actual_enlace.siguiente
                else:
                    actual_enlace = actual_enlace.siguiente
            contenido_enlace_rank += '}\n'
            
        rango_columna = int(dim_y)   
        for j in range(rango_columna):   
            while actual_enlace_2 is not None:
                if actual_enlace_2.indice_terreno is indice_terreno:
                    if str(int(actual_enlace_2.x)+1) <= dim_x:
                        contenido_enlace_nodo_c += 'nodo'+actual_enlace_2.x+'_'+actual_enlace_2.y+' -> nodo'+str(int(actual_enlace_2.x)+1)+'_'+actual_enlace_2.y+';\n'
                    actual_enlace_2 = actual_enlace_2.siguiente
                else:
                    actual_enlace_2 = actual_enlace_2.siguiente
            
        contenido += contenido_enlace_f
        contenido += contenido_enlace_nodo_f
        contenido += contenido_enlace_c   
        contenido += contenido_enlace_rank    
        contenido += contenido_enlace_nodo_c 
        #print(contenido)      
        return contenido              
                 
    def ver_ruta(self, indice_terreno):
        actual = self.inicio
        final = self.final
        actual_tamano = self.inicio
        posicion_elegida = None
        global inicio_x 
        global inicio_y 
        global fin_x 
        global fin_y
        global dim_x
        global dim_y
        global combustible
        posicion_actual = None
        gasto_combustible = 0
        contador = 0
        
        tamano_terreno = int(dim_x)*int(dim_y)
        print('\ntamaño terreno',tamano_terreno,'\n')
        self.contenido_lateral()
        while actual_tamano is not None:
            if actual_tamano.indice_terreno is indice_terreno:
                if inicio_x is actual_tamano.x and inicio_y is actual_tamano.y:
                    actual = actual_tamano
                    print('actual',actual.valor)
                elif fin_x is actual_tamano.x and fin_y is actual_tamano.y:
                    final = actual_tamano
                    print('final',final.valor)
            actual_tamano = actual_tamano.siguiente
        gasto_combustible += int(actual.valor)  
        
        while actual is not final:
            if actual.indice_terreno is indice_terreno:
                valor_derecha = True 
                valor_izquierda = True
                valor_abajo = False
                valor_arriba = True
                w = self.inicio   
                s = actual     
                up = None
                down = None
                print('\n....................')
                print("Actual valor: ",actual.valor)  
                #----------Derecha-------------            
                tmp = actual.siguiente
                right = tmp
                if tmp is None:
                    right is None
                    valor_derecha = False
                if tmp.y < actual.y:
                    right is None
                    valor_derecha = False
                
                if right is not None:
                    print('Derecha valor: ',right.valor,' - x:', right.x,' - y:', right.y)    
                #----------Izquierda-------------
                tmp2 = actual.anterior
                left = tmp2  
                if tmp2 is None:
                    left = None
                    valor_izquierda = False
                if tmp2.y > actual.y:
                    left = None
                    valor_izquierda = False
                
                if left is not None:
                    print('Izquierda valor: ',left.valor,' - x:', left.x,' - y:', left.y)      
                #----------Abajo-------------
                id_abajo = actual.id + int(dim_y)
                while s is not None:
                    if s.indice_terreno == indice_terreno:
                        if id_abajo == s.id:
                            valor_abajo = True
                            down = s
                            break
                    s = s.siguiente
                
                if down is not None:
                    print('Abajo valor: ',down.valor,' - x:', down.x,' - y:', down.y) 
                #----------Arriba-------------
                id_arriba = actual.id - int(dim_y)
                while w is not None:
                    if w.indice_terreno == indice_terreno:
                        if int(actual.x) == 1:
                            valor_arriba = False
                            break
                        if id_arriba is w.id:
                            up = w
                            print('Arriba valor: ',up.valor,' - x:', up.x,' - y:', up.y)
                            break
                        w = w.siguiente 
                    else:    
                        w = w.siguiente  
                
                posiciones = []
                if valor_abajo:
                    nuevo_abajo = Robot(down, down.valor, 'Abajo')
                    posiciones.append(nuevo_abajo)
                if valor_derecha:
                    nuevo_derecha = Robot(right, right.valor, 'Derecha')
                    posiciones.append(nuevo_derecha)
                if valor_izquierda:
                    nuevo_izquierda = Robot(left, left.valor, 'Izquierda')
                    posiciones.append(nuevo_izquierda)
                if valor_arriba:
                    nuevo_arriba = Robot(up, up.valor, 'Arriba')
                    posiciones.append(nuevo_arriba)
                
                self.ordenamiento(posiciones)
                                       
                k = 0
                for k in range(len(posiciones)):
                    pos = posiciones[k].posicion
                    print('lista:',posiciones[k].nombre,' valor -',pos.valor,' - x:',pos.x,' - y:', pos.y )
                    k += 1  
                
                i = 0
                for i in range(len(posiciones)):  
                    if posicion_elegida is not None or posicion_actual is not None:
                        posicion_elegida = posiciones[i].posicion
                        if posicion_elegida.entro is False:
                            break
                        #if posicion_elegida.id is posicion_actual.id or posicion_elegida.entro is True:
                            #posicion_elegida = posiciones[i].posicion
                        #else:
                         #   break
                    else:
                        posicion_elegida = posiciones[i].posicion
                        break
                posicion_actual = actual  
                    
                print("elegido:",posicion_elegida.valor,' - x:',posicion_elegida.x,' - y',posicion_elegida.y) 
                gasto_combustible += int(posicion_elegida.valor)
                actual.setEntro(True)
                posiciones.clear()     
                actual = posicion_elegida 
                if actual is final: 
                    final.setEntro(True)  
                    
                if contador == tamano_terreno:
                    print('\t \t \t¡ALERTA! \n<<<<<Lastimosamente hemos perdido comunicación con r2e2!')
                    print('Se ha extraviado en su viaje por los inhóspitos terrenos>>>>>')
                    print('\n\t\t<<<<<Gasto combustible>>>>>','\n\t\t\t    ',gasto_combustible)
                    combustible -= gasto_combustible
                    print('\n\t\t<<<<<Combustible Sobrante>>>>>''\n\t\t\t    ',combustible,'\n')
                    return
                contador += 1
                    
            else:
                actual = actual.siguiente 
            if actual is None:
                print('nooooooooooooooooooooooneeeeeeee')
        print('\n<<<<<Gasto combustible>>>>>',gasto_combustible)
        combustible -= gasto_combustible
        print('\n<<<<<Combustible Sobrante>>>>>',combustible)
               
    def ordenamiento(self,posiciones):
        for i in range(1,len(posiciones)):
            for j in range(0,len(posiciones)-i):
                if (posiciones[j+1].valor < posiciones[j].valor):
                    aux = posiciones[j].valor
                    aux2 = posiciones[j].posicion
                    aux3 = posiciones[j].nombre
                    posiciones[j].valor = posiciones[j+1].valor
                    posiciones[j].posicion = posiciones[j+1].posicion
                    posiciones[j].nombre = posiciones[j+1].nombre
                    posiciones[j+1].valor = aux 
                    posiciones[j+1].posicion = aux2 
                    posiciones[j+1].nombre = aux3 
    
    
                