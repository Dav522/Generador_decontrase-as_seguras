# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 23:07:01 2025

@author: Estacion X3
"""

import random
import os          # Para limpiar la pantalla
import time        # Animacion
import shutil      # Para centrar el título según el ancho de la terminal 

opcion = ""

while opcion != "0":
    # ====== ESTÉTICA: limpiar pantalla ======
    os.system("cls" if os.name == "nt" else "clear")

    # ====== ESTÉTICA: encabezado centrado con marco ======
    cols = shutil.get_terminal_size((80, 20)).columns  # ancho de terminal (80 por defecto si no se puede obtener)
    titulo = " Generador de Contraseñas "
    borde = "=" * len(titulo)
    print(borde.center(cols))
    print(titulo.center(cols))
    print(borde.center(cols))
    print()  # línea en blanco

    # ===== Menú principal =====
    print("1.- Generar contraseña segura aleatoria")
    print("2.- Generar contraseña segura específica")
    print("0.- Salir")
    print("-" * 40)  # separador estético
    opcion = input("Elige una opción: ").strip()

    # ========= Opción 1: contraseña aleatoria simple =========
    if opcion == "1":
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        # Validación de longitud (básica, sin try/except)
        while True:
            longitud_txt = input("¿Número de caracteres?: ").strip()
            if not longitud_txt.isdigit():
                print("Longitud inválida. Debe ser un número entero.")
                continue
            longitud = int(longitud_txt)
            if longitud <= 0 or longitud > 64:
                print("Usa una longitud entre 1 y 64.")
                continue
            break

        # ESTÉTICA: pequeña “animación” de generación
        print("\nGenerando", end="", flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")

        contraseña = ""
        for i in range(longitud):
            contraseña += random.choice(caracteres)

        # ESTÉTICA: resultado con caja simple
        caja = "-" * (len(contraseña) + 8)
        print(caja)
        print(f"|  {contraseña}  |")
        print(caja)
        input("\n(Enter para volver al menú) ")

    # ========= Opción 2: contraseña específica (con tuplas y lista) =========
    elif opcion == "2":
        tipos_disponibles = (
            ("minúsculas", "abcdefghijklmnopqrstuvwxyz"),
            ("MAYÚSCULAS", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            ("números",    "0123456789"),
            ("símbolos",   "!@#$%^&*()-_=+[]{}<>?")
        )

        seleccionados = []

        print("\nConfigura tu contraseña específica (responde s/n):")
        print("-" * 40)
        for nombre, conjunto in tipos_disponibles:
            r = input(f"¿Incluir {nombre}? (s/n): ").strip().lower()
            if r == "s":
                seleccionados.append(conjunto)

        if len(seleccionados) == 0:
            print("\nDebes seleccionar al menos un tipo de carácter.")
            input("(Enter para volver al menú) ")
            continue

        caracteres = "".join(seleccionados)

        while True:
            longitud_txt = input("¿Número de caracteres?: ").strip()
            if not longitud_txt.isdigit():
                print("Longitud inválida. Debe ser un número entero.")
                continue
            longitud = int(longitud_txt)
            if longitud <= 0 or longitud > 64:
                print("Usa una longitud entre 1 y 64.")
                continue
            break

        # ESTÉTICA: pequeña “animación” de generación
        # Uso de funcion de animación 
        print("\nGenerando", end="", flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")

        contraseña = ""
        for i in range(longitud):
            contraseña += random.choice(caracteres)

        caja = "-" * (len(contraseña) + 8)
        print(caja)
        print(f"|  {contraseña}  |")
        print(caja)
        input("\n(Enter para volver al menú) ")

    elif opcion == "0":
        print("\nGracias por preferirnos\n")
        time.sleep(0.6)  # pausa breve para que se vea el mensaje y la animacion

    else:
        print("\nOpción incorrecta")
        time.sleep(0.8)  # pausa breve y vuelve al menú y se borra la pantalla