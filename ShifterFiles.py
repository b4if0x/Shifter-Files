from ast import Or
import os
from os.path import isfile, join
import random, string

"""Declaramos las funciones principales"""

def limpiar():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def cambiador (target):
    contador=0
    contadorOmitidos=0
    for nombre_directorio, subdirs, ficheros in os.walk(target):
        for nombre_fichero in ficheros:
            contador = contador +1
            if join(nombre_directorio,nombre_fichero)!=join(target,nombre_fichero):
                try:
                    os.rename(join(nombre_directorio,nombre_fichero),join(target,nombre_fichero))
                except FileExistsError:
                    forcedName=random.choice(string.ascii_letters)+nombre_fichero
                    os.rename(join(nombre_directorio,nombre_fichero),join(target,forcedName))
            else:
                contadorOmitidos=contadorOmitidos+1
    return contador, contadorOmitidos

def presentacion(): 
    limpiar()
    print("****************************************") 
    print("*                                      *")
    print("*        Mover todo a la raiz          *")
    print("*                                      *")
    print("****************************************")
    target = input("Introduce ruta: ")   
    contador, contadorOmitidos=cambiador(target)     
    print('Ficheros totales: ',contador, ' Omitidos: ', contadorOmitidos, ' Movidos: ', contador-contadorOmitidos)        

def iniciando():
    limpiar()
    print("****************************************") 
    print("*                                      *")
    print("*           Shifter Files v1           *")
    print("*                                      *")
    print("****************************************")
    print("1-Mover ficheros a raíz")
    print("2-Salir del programa")
    print(" ")
    opcion=input("Selecciona una opcion [1 o 2]: ")
    match opcion:
        case "1":  
            presentacion()
        case "2":
            print("-Saliendo del programa-")
            exit
        case _:
            iniciando()
"""Lanzamos el programa"""            
iniciando()
