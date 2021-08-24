import xml.etree.ElementTree as ET
from ListaDoble import ListaDoble

terrenos = ListaDoble() 
posiciones = ListaDoble()

def leer_archivo():
    #ruta = str(input('Ingrese la Ruta del Archivo: '))
    ruta = 'entrada.xml'
    with open(ruta, 'rt',encoding='utf-8') as f:
        tree = ET.parse(f)
        root = tree.getroot()
    
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
        #print(contador_pos, contador_id, posx, posy, valor)
        posiciones.insertar(contador_pos, contador_id, posx, posy, valor)          
           
def datos_estudiante():
    print('\t> Arnoldo Luis Antonio González Camey')
    print('\t> 201701548')
    print('\t> Introducción a la Programación y Computación 2 Sección \"D\"')
    print('\t> Ingeniería en Ciencias y Sistemas')
    print('\t> 4to Semestre')

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

def procesar_terreno():
    nombre_terreno = input("Escribe el nombre del terreno a procesar: ") 
    indice_terreno = terrenos.buscar_terreno(nombre_terreno)
    print('indice: ',indice_terreno)
    posiciones.mostrar_posiciones(indice_terreno)
    terrenos.datos_terreno(indice_terreno)
    posiciones.ver_ruta(indice_terreno)    
            
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
            procesar_terreno()
        elif opcion == 3:
            print('\nOpción Escribir Archivo Salida:')
        elif opcion == 4:
            print('\nOpción Datos del Estudiante:')
            datos_estudiante()
        elif opcion == 5:
            print('\nOpción Generar Gráfica')
        elif opcion == 6:
            termino = True
            exit() 
        else:
            print('Elige una opción correcta')
            
if __name__ == '__main__':
    main()   