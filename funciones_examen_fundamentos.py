import json
import random
import statistics
import numpy as np

def mostrar_menu():
    
    print("Programa de análisis de sueldos")
    print("-------------------------------------------")
    print("1-Asignar sueldos aleatorios")
    print("2-Clasificar sueldos")
    print("3-Ver estadisticas")
    print("4-Reportes de sueldos")
    print("5-Salir")
    print("-------------------------------------------")
    
    return

def generacion_sueldos_aleatorios(trabajadores, siguiente_fila):
    print("")
    print("A continuación se asginarán los sueldos de forma aleatoria.")

    for i in range(10):
        if i == 0:
            trabajadores[siguiente_fila,0] = "Juan Perez"
        elif i == 1:
            trabajadores[siguiente_fila,1] = "Maria Garcia"    
        elif i == 2: 
            trabajadores[siguiente_fila,2] = "Carlos Lopez"
        elif i == 3:
            trabajadores[siguiente_fila,3] = "Ana Martinez"
        elif i == 4:
            trabajadores[siguiente_fila,4] = "Pedro Rodriguez"
        elif i == 5:
            trabajadores[siguiente_fila,5] = "Laura Hernandez"
        elif i == 6:
            trabajadores[siguiente_fila,6] = "Miguel Sanchez"
        elif i == 7:
            trabajadores[siguiente_fila,7] = "isabel Gomez"
        elif i == 8:
            trabajadores[siguiente_fila,8] = "Francisco Diaz"
        elif i == 9:
            trabajadores[siguiente_fila,9] = "Elena Fernandez"
        print("")
        
    return trabajadores


def clasificar_sueldos():
     print

def ver_estadisticas():
     print("Estas son las estadisticas de los sueldos de la empresa: ")


def reporte_de_sueldos():
     print
     

def leer_json(archivo_json):
    try:
        with open(archivo_json, 'r') as file:
            trabajadores = np.array(json.load(file), dtype="object")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        trabajadores = np.empty((2, 10), dtype="object")
    return trabajadores        

def sobreescribir_json(trabajadores, archivo_json):
    with open(archivo_json, 'w') as file:
            json.dump(trabajadores, file, indent=4)
            print("Gracias por utilizar el Programa de análisis de sueldos")