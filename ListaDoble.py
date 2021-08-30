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
gasto_combustible = 0

class ListaDoble():
  
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0
        self.inicio_terreno = None
        self.final_terreno = None
        self.size_terreno = 0
        self.inicio_robot = None
        self.final_robot = None
        self.size_robot = 0
                
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
            
    def insertar_robot(self, posicion, valor, nombre): 
        nuevo = Robot(posicion, valor, nombre)
        self.size_robot += 1
        if self.inicio_robot is None:
            self.inicio_robot = nuevo
            self.final_robot = nuevo
        else:
            tmp = self.inicio_robot
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
            self.final_robot = nuevo                         

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
        datos_terreno = ''
        actual_ter = self.inicio_terreno
        while actual_ter is not None:
            if int(indice_terreno) == int(actual_ter.indice):
                datos_terreno = actual_ter.nombre + '_' + actual_ter.dimension_x + 'x' + actual_ter.dimension_y
                return datos_terreno
            actual_ter = actual_ter.siguiente
        return 'Nombre Desconocido'              
    
    def buscar_nombre_terreno_grafica(self):
        actual_ter = self.inicio_terreno
        i = 0
        while actual_ter is not None:
            print(i+1,')',actual_ter.nombre)
            i += 1
            actual_ter = actual_ter.siguiente        
         
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
    
    def datos_salida_terreno(self,indice_terreno):
        global gasto_combustible
        actual_datos = self.inicio_terreno
        contenido = ''
        while actual_datos is not None:
            if actual_datos.indice is indice_terreno:
                contenido += '\n\t<dimension>\n\t\t<m>'+actual_datos.dimension_x+'</m>\n\t\t<n>'+actual_datos.dimension_y+'</n>\n\t</dimension>\n'
                contenido += '\t<posicioninicio>\n\t\t<x>'+actual_datos.incio_x+'</x>\n\t\t<y>'+actual_datos.incio_y+'</y>\n\t</posicioninicio>\n'
                contenido += '\t<posicionfin>\n\t\t<x>'+actual_datos.final_x+'</x>\n\t\t<y>'+actual_datos.final_y+'</y>\n\t</posicionfin>\n'
                contenido += '\t<combustible>'+str(gasto_combustible)+'</combustible>\n'
                break
            actual_datos = actual_datos.siguiente
        return contenido
    
    def datos_salida_posicion(self, indice_terreno):
        actual_posicion = self.inicio
        contenido = ''
        while actual_posicion is not None:
            if actual_posicion.indice_terreno is indice_terreno:
                if actual_posicion.entro:
                    contenido += '\t<posicion x=\"'+actual_posicion.x+'\" y=\"'+actual_posicion.y+'\">'+actual_posicion.valor+'</posicion>\n'
            actual_posicion = actual_posicion.siguiente
        contenido += '</terreno>'
        return contenido
    
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
        actual = self.inicio
        actual_enlace = self.inicio
        actual_enlace_2 = self.inicio
        
        while actual is not None:
            if int(actual.indice_terreno) == int(indice_terreno):
                tmp = actual.siguiente
                if tmp is None:
                    if termino:
                        if actual.entro: 
                            contenido += 'nodo'+actual.x+'_'+actual.y+'[label=\"1\",fillcolor=green,group='+str(int(actual.y) + 1)+']\n'
                        else:
                            contenido += 'nodo'+actual.x+'_'+actual.y+'[label=\"O\",fillcolor=gray,group='+str(int(actual.y) + 1)+']\n'
                    else: 
                        contenido += 'nodo'+actual.x+'_'+actual.y+'[label=\"'+actual.valor+'\",fillcolor=green,group='+str(int(actual.y) + 1)+']\n'
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
            contenido_enlace_rank += '\n{rank = same;F'+str(i+1)      
            while actual_enlace is not None:
                if int(actual_enlace.indice_terreno) == int(indice_terreno):
                    tmp = actual_enlace.siguiente
                    if tmp is None:
                        if str(actual_enlace.x) == str(i+1):
                            contenido_enlace_rank += ';nodo'+actual_enlace.x+'_'+actual_enlace.y+''
                        else:
                            break
                        break
                    if str(actual_enlace.x) == str(i+1):
                        contenido_enlace_rank += ';nodo'+actual_enlace.x+'_'+actual_enlace.y+''
                    else:
                        break
                    
                    actual_enlace = actual_enlace.siguiente
                else:
                    actual_enlace = actual_enlace.siguiente
            contenido_enlace_rank += '}'
            
        rango_columna = int(dim_y)   
        for j in range(rango_columna):   
            while actual_enlace_2 is not None:
                if int(actual_enlace_2.indice_terreno) == int(indice_terreno):
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
        global gasto_combustible
        gasto_combustible = 0
        contador = 0
        
        print('\n\n- Calculando el tamaño del terreno')
        tamano_terreno = int(dim_x)*int(dim_y)
        print('\n<<<Tamaño Terreno>>>\n',tamano_terreno)
        while actual_tamano is not None:
            if actual_tamano.indice_terreno is indice_terreno:
                if inicio_x is actual_tamano.x and inicio_y is actual_tamano.y:
                    actual = actual_tamano
                elif fin_x is actual_tamano.x and fin_y is actual_tamano.y:
                    final = actual_tamano
            actual_tamano = actual_tamano.siguiente
        gasto_combustible += int(actual.valor)  
        
        print('\n- Calculando la ruta')
        if combustible > 0:
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
                    #print("Actual valor: ",actual.valor)  
                    #----------Derecha-------------            
                    tmp = actual.siguiente
                    right = tmp
                    if tmp is None:
                        right is None
                        valor_derecha = False
                    if tmp.y < actual.y:
                        right is None
                        valor_derecha = False
                    
                    #if right is not None:
                        #print('Derecha valor: ',right.valor,' - x:', right.x,' - y:', right.y)    
                    #----------Izquierda-------------
                    tmp2 = actual.anterior
                    left = tmp2  
                    if tmp2 is None:
                        left = None
                        valor_izquierda = False
                    if tmp2.y > actual.y:
                        left = None
                        valor_izquierda = False
                    
                    #if left is not None:
                        #print('Izquierda valor: ',left.valor,' - x:', left.x,' - y:', left.y)      
                    #----------Abajo-------------
                    id_abajo = actual.id + int(dim_y)
                    while s is not None:
                        if s.indice_terreno == indice_terreno:
                            if id_abajo == s.id:
                                valor_abajo = True
                                down = s
                                break
                        s = s.siguiente
                    
                    #if down is not None:
                        #print('Abajo valor: ',down.valor,' - x:', down.x,' - y:', down.y) 
                    #----------Arriba-------------
                    id_arriba = actual.id - int(dim_y)
                    while w is not None:
                        if w.indice_terreno == indice_terreno:
                            if int(actual.x) == 1:
                                valor_arriba = False
                                break
                            if id_arriba is w.id:
                                up = w
                                #print('Arriba valor: ',up.valor,' - x:', up.x,' - y:', up.y)
                                break
                            w = w.siguiente 
                        else:    
                            w = w.siguiente  
             
                    if valor_abajo:
                        self.insertar_robot(down, down.valor, 'Abajo')
                    if valor_derecha:
                        self.insertar_robot(right, right.valor, 'Derecha')
                    if valor_izquierda:
                        self.insertar_robot(left, left.valor, 'Izquierda')
                    if valor_arriba:
                        self.insertar_robot(up, up.valor, 'Arriba')
                    
                    posicion_elegida = self.BubbleSort(posicion_elegida)
                    #print("elegida:",posicion_elegida.valor,' - x:',posicion_elegida.x,' - y',posicion_elegida.y) 
                    gasto_combustible += int(posicion_elegida.valor)
                    actual.setEntro(True)  
                    actual = posicion_elegida 
                    
                    if actual is final: 
                        final.setEntro(True)  
                        
                    if contador == tamano_terreno:
                        print('\t \t \t¡ALERTA! \n<<<Lastimosamente hemos perdido comunicación con R2e2!')
                        print('Se ha extraviado en su viaje por los inhóspitos terrenos>>>')
                        print('\n<<<Gasto combustible>>>\n',gasto_combustible)
                        combustible -= gasto_combustible
                        print('\n<<<Combustible Sobrante>>>\n',combustible,'\n')
                        return
                    contador += 1
                        
                else:
                    actual = actual.siguiente 
                if actual is None:
                    print('Fin')
            print('\n<<<Gasto combustible>>>\n',gasto_combustible)
            combustible -= gasto_combustible
            print('\n<<<Combustible Sobrante>>>\n',combustible,'\n')
        else:
            print('\t \t \t¡ALERTA! \n<<<El Robot R2e2 se ha quedado sin combustible>>>\n')
            print('<<<Combustible Sobrante>>>\n0')
    
    def limpieza(self):
        actual_limpieza = self.inicio
        while actual_limpieza is not None:
            actual_limpieza.setEntro(False)
            actual_limpieza = actual_limpieza.siguiente
                   
    def BubbleSort(self, posicion_elegida):
        actual = self.inicio_robot
        if self.size_robot > 1:
            while True:
                actual = self.inicio_robot
                ant = None 
                sig = self.inicio_robot.siguiente  
                cambio = False
                while sig != None:
                    if actual.valor > sig.valor:
                        cambio = True
                        if ant != None:
                            tmp = sig.siguiente
                            ant.siguiente = sig
                            sig.siguiente = actual
                            actual.siguiente = tmp
                        else:
                            tmp2 = sig.siguiente
                            self.inicio_robot = sig
                            sig.siguiente = actual
                            actual.siguiente = tmp2
                        ant = sig
                        sig = actual.siguiente
                    else:
                        ant = actual
                        actual = sig
                        sig = sig.siguiente
                if not cambio:
                    break
        actual = self.inicio_robot
        while actual is not None:
            posicion_elegida = actual.posicion
            if posicion_elegida.entro is False:
               break
            else:
                actual = actual.siguiente 
        self.inicio_robot = None
        self.final_robot = None  
        return posicion_elegida    