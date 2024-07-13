import json
import random
import statistics
import numpy as np
from funciones_examen_fundamentos import *

trabajadores=np.empty([2,10],dtype="object")

archivo_json = "trabajadores.json"

trabajadores = np.array(leer_json(archivo_json), dtype="object")

while True:
    
    mostrar_menu()
    print(trabajadores)
    try:
        opcion = int(input("¿Qué acción desea realizar? "))
     
        if opcion == 1:
            siguiente_fila = 0
            while trabajadores[siguiente_fila, 0] is not None:
                siguiente_fila += 1
        
        elif opcion == 2:
            print
        
        elif opcion == 3:
            print
    
        elif opcion == 4:
            print

        elif opcion == 5:
            sobreescribir_json(trabajadores.tolist(), archivo_json)
            break

        else:
            print("")
            print("Favor ingrese una opción válida")
            print("")
        
    except ValueError:
        print("Por favor, ingrese un número válido.")