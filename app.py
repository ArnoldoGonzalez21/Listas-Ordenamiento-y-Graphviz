def leerArchivo():
    try:
        fichero = str(input('Ingrese la Ruta del Archivo:'))
        data = ''
        with open(fichero, "r", encoding='utf-8') as archivo:
            print(fichero)
            data = archivo.read()
            print('\nArchivo Cargado exitosamente')
            print(data)
            data += '°' #saber donde termina el archivo
        data_limpio = data.strip() #eliminar espacios del final y principio
        #estudiantes.clear() #resetear lista
        #recorrerStr(data_limpio)
    except OSError:
        print("No se pudo leer el Archivo")
        exit()
        
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
            print('Opción Cargar Archivo:')
            leerArchivo()
        elif opcion == 2:
            print(2)
        elif opcion == 3:
            print(3)
        elif opcion == 4:
            print('\nOpción Datos del Estudiante:')
            datos_estudiante()
        elif opcion == 5:
            print(5)
        elif opcion == 6:
            termino = True
            exit() 
        else:
            print('Elige una opción correcta')
            
if __name__ == '__main__':
    main()   