# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 23:07:01 2025

@author: Estacion X3
"""

import random

opcion=""

while opcion != "0":

    print("Menu Inicial")
    print ("1.- Generar contraseña segura aleatoria")
    print("2.-Generar contraseña segura especifica")
    print("0.- Salir")
    
    opcion = input("Elige una opcion:")
    
    if opcion =="1":
        
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
        longitud = int(input("¿Dime el numero de caracteres que quieres en tu contraseña"))
        
        contraseña=""
        
        for i in range(longitud):
            contraseña += random.choice(caracteres)
            
        print ("La contraseña es", contraseña)
     
    elif opcion=="0":
        
        print("Gracias por preferirnos")
        
    else:
        print("Opción incorrecta")
    