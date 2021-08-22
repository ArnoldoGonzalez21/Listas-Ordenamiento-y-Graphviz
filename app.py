from typing import List
import xml.etree.ElementTree as ET
from ListaDoble import ListaDoble

combustible = 9999

def leerArchivo():
    #ruta = str(input('Ingrese la Ruta del Archivo: '))
    ruta = 'entrada.xml'
    with open(ruta, 'rt',encoding='utf-8') as f:
        tree = ET.parse(f)
        root = tree.getroot()
    #for elem in root:      #nombre del terreno
     #   print(elem.attrib)
    
    posiciones = ListaDoble()
    for node in root.iter('posicion'):
        posx = node.attrib.get('x')
        posy = node.attrib.get('y')
        valor = node.text
        """if posx and posy:
            print('x: '+posx)
            print('y: '+posy)
            print('valor: '+valor)"""
        posiciones.insertar(posx, posy, valor)
    
    posiciones.showPos()
    posiciones.verRuta()
    
    
    #for name in root.findall("terreno/dimension/m"): #buscar elementos
     #   print(name.text)                        #el contenido es text y tag es la etiqueta
        
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
            leerArchivo()
        elif opcion == 2:
            print('\nOpción Procesar Terreno:')
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
    leerArchivo()   