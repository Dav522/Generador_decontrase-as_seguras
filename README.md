# Generador_decontraseñas_seguras
Proyecto de generador de contraseñas 
# Generador de Contraseñas en Python

Este proyecto es un **generador de contraseñas seguras** desarrollado en Python por el estudiante David Armas como parte del proyecto final de Lógica de Programación.  
El programa tiene estructuras condicionales, bucles, listas y tuplas, además de elementos básicos de procesamiento de datos y hace uso de librerias y funciones.

---
 Funcionalidad

 1. Menú principal
- Se mantiene activo con un **bucle `while`** hasta que el usuario escriba la opcion `0` (salir).
- Opción inválida → existe un mensaje de error.

 2. Generar contraseña aleatoria
- Usa un **conjunto fijo de caracteres** (letras y números).
- Solicita al usuario la longitud de la contraseña.
- Construye la contraseña con un **bucle `for`** y haciendo uso de la libreria random y la funcion choice
- Incluye **validaciones básicas**: longitud debe ser un número entero entre 1 y 64.

 3. Generar contraseña específica
- Permite elegir si incluir:
  - Minúsculas
  - Mayúsculas
  - Números
  - Símbolos
- Implementado con:
  - **Tupla de tuplas** → define las categorías disponibles.
  - **Lista** → almacena las elecciones del usuario.
- El programa une las elecciones y genera la contraseña con `for + random.choice`.
- Validación: para que funcione al  menos una categoría debe estar seleccionada.

4. Validaciones y control de flujo
- Uso de condicionales `if / elif / else`.
- Uso de operadores relacionales y lógicos (`==`, `!=`, `>`, `and`, `or`).
- Uso de **alteradores de bucle**: `continue` para reintentar entradas inválidas.

 5. Estética (librerías estándar)
- `os` → limpiar pantalla entre menús.
- `time` → pequeñas pausas para simular animación de “generando...”.
- `shutil` → centrar el título según el ancho de la terminal.
- Resultados enmarcados con **cajas de guiones**.

---

 Estructura del Proyecto

