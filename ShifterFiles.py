from ast import Or
import os
from os.path import isfile, join
import random, string

"""Declaring functions"""

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
    print("*        Moving to Root Patch          *")
    print("*                                      *")
    print("****************************************")
    target = input("Introduce ruta: ")   
    if os.path.exists(target):
        contador, contadorOmitidos=cambiador(target)     
        print('Total: ',contador, ' Omitted: ', contadorOmitidos, ' Moved: ', contador-contadorOmitidos)
    else:
        print('The patch does not exist. Try again pressing a key.')
        input()
        presentacion()

def iniciando():
    limpiar()
    print("****************************************") 
    print("*                                      *")
    print("*           Shifter Files v1.1         *")
    print("*                                      *")
    print("****************************************")
    print("1-Move files to root")
    print("2-Exit")
    print(" ")
    opcion=input("Choose a option [1 or 2]: ")
    match opcion:
        case "1":  
            presentacion()
        case "2":
            print("-Leaving the program-")
            exit
        case _:
            iniciando()
"""Launching main function"""            
iniciando()
