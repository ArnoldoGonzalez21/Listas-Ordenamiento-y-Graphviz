import xml.etree.ElementTree as ET
from os import startfile, system
from ListaDoble import ListaDoble

terrenos = ListaDoble() 
posiciones = ListaDoble()
indice_terreno = -1

def leer_archivo():
    ruta = str(input('Ingrese la Ruta del Archivo: '))
    try:
        with open(ruta, 'rt',encoding='utf-8') as f:
            tree = ET.parse(f)
            root = tree.getroot()
    except OSError:
        print("<<< No se pudo leer el Archivo "+ruta+' >>>')
        return
        
    contador = 0
    for elem in root:      
        nombre = elem.get('nombre') #nombre del terreno
        dim_x = elem.findtext('dimension/m') #dimension x del terreno
        dim_y = elem.findtext('dimension/n') #dimension y del terreno                  
        inicio_x = elem.findtext('posicioninicio/x') #incio x 
        inicio_y = elem.findtext('posicioninicio/y') #incio y 
        final_x = elem.findtext('posicionfin/x') #fin x 
        final_y = elem.findtext('posicionfin/y') #fin y         
        terrenos.insertar_terrenos(contador,nombre,dim_x,dim_y,inicio_x,inicio_y,final_x,final_y)
        contador += 1
    
    contador_id = 1
    contador_pos = -1
    for node in root.iter('posicion'):        
        posx = node.attrib.get('x')
        posy = node.attrib.get('y')
        valor = node.text
        contador_id += 1
        if int(posx) == 1 and int(posy) == 1:
            contador_pos +=1
            contador_id = 1
        posiciones.insertar(contador_pos, contador_id, posx, posy, valor, False)          
           
def datos_estudiante():
    print('\t> Arnoldo Luis Antonio González Camey')
    print('\t> 201701548')
    print('\t> Introducción a la Programación y Computación 2 Sección \"D\"')
    print('\t> Ingeniería en Ciencias y Sistemas')
    print('\t> 6to Semestre')

def pedir_numero():
    correcto = False
    numero = 0
    while(not correcto):
        try:
            correcto = True
            numero = int(input("Elige una opción: "))            
        except ValueError:
            print('Elige un número')
    return numero

def procesar_terreno(grafica):
    global indice_terreno
    if grafica:
        posiciones.limpieza()
        terrenos.buscar_nombre_terreno_grafica()
        indice_terreno = input("Digite el número de la ruta del terreno a graficar: ") 
        indice_terreno = int(indice_terreno) - 1
    else:
        posiciones.limpieza()        
        nombre_terreno = input("Escribe el nombre del terreno a procesar: ") 
        indice_terreno = terrenos.buscar_terreno(nombre_terreno)
    posiciones.mostrar_posiciones(indice_terreno)
    terrenos.datos_terreno(indice_terreno)
    posiciones.ver_ruta(indice_terreno)
    if grafica is False:  
        print('<<<Camino Elegido por R2e2 en',nombre_terreno,'>>>') 
    posiciones.mostrar_posiciones_camino(indice_terreno) 
    if grafica:
        generarGraphviz(indice_terreno,False)
        generarGraphviz(indice_terreno,True)

def escribir_archivo():
    global indice_terreno
    if indice_terreno != -1:
        ruta = str(input('Ingrese la Ruta Relativa del Archivo: '))
        nombre_terreno = terrenos.buscar_nombre_terreno(indice_terreno)
        inicio_xml = '<terreno nombre=\"'+ nombre_terreno + '\">'
        datos_salida_terreno = terrenos.datos_salida_terreno(indice_terreno)
        datos_salida_posicion = posiciones.datos_salida_posicion(indice_terreno)
        contenido = inicio_xml + datos_salida_terreno + datos_salida_posicion
        miArchivo= open(ruta,'w')
        miArchivo.write(contenido)
        miArchivo.close()
        print('Se generó el archivo correctamente')
    else:
        print('Elige el terreno a procesar')

def generarGraphviz(indice, termino):
    indice = str(indice)
    nombre_terreno = terrenos.buscar_nombre_terreno(indice)
    inicio_graphviz = '''
    digraph L{
        node[shape = circle fillcolor="white" style = filled]
        subgraph cluster_p{
            label = \"'''+nombre_terreno+''' \"
            bgcolor = "#398D9C"
            raiz[label = "0,0"]
            edge[dir = "both"]
        '''
    lateral = posiciones.contenido_lateral()
    
    nodos = posiciones.enlazar_nodos(indice, termino)
    final_graphviz = '}   }'
    graphviz = inicio_graphviz + lateral + nodos + final_graphviz
    #print(graphviz)
    if termino:
        miArchivo= open('graphviz_explorado_'+indice+'.dot','w')
        miArchivo.write(graphviz)
        miArchivo.close()
        system('dot -Tpng graphviz_explorado_'+indice+'.dot -o Terreno_explorado_'+indice+'.png')
        system('cd ./Terreno_explorado_'+indice+'.png')
        startfile('Terreno_explorado_'+indice+'.png')
    else:
        miArchivo= open('graphviz_inexplorado_'+indice+'.dot','w')
        miArchivo.write(graphviz)
        miArchivo.close()
        system('dot -Tpng graphviz_inexplorado_'+indice+'.dot -o Terreno_inexplorado_'+indice+'.png')
        system('cd ./Terreno_inexplorado_'+indice+'.png')
        startfile('Terreno_inexplorado_'+indice+'.png')
                  
def main():
    termino = False
    opcion = 0   
    while not termino:
        print('\n<<<<<<<<<< Menú >>>>>>>>>>')
        print ("1. Cargar Archivo")
        print ("2. Procesar Terreno")
        print ("3. Escribir Archivo Salida")
        print ("4. Mostrar Datos del Estudiante")
        print ("5. Generar Gráfica")
        print ("6. Salir")
        opcion = pedir_numero() 
        if opcion == 1:
            print('\nOpción Cargar Archivo:')
            leer_archivo()
        elif opcion == 2:
            print('\nOpción Procesar Terreno:')
            procesar_terreno(False)
        elif opcion == 3:
            print('\nOpción Escribir Archivo Salida:')
            escribir_archivo()
        elif opcion == 4:
            print('\nOpción Datos del Estudiante:')
            datos_estudiante()
        elif opcion == 5:
            print('\nOpción Generar Gráfica')
            procesar_terreno(True)
        elif opcion == 6:
            termino = True
            exit() 
        else:
            print('Elige una opción correcta')
            
if __name__ == '__main__':
    main()   