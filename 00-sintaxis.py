#/*
# * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
# * - Recuerda que todas las instrucciones de participación están en el
# *   repositorio de GitHub.
# *
# * Lo primero... ¿Ya has elegido un lenguaje?
# * - No todos son iguales, pero sus fundamentos suelen ser comunes.
# * - Este primer reto te servirá para familiarizarte con la forma de participar
# *   enviando tus propias soluciones.
# *
# * EJERCICIO:
# * - Crea un comentario en el código y coloca la URL del sitio web oficial del
# *   lenguaje de programación que has seleccionado.
# * - Representa las diferentes sintaxis que existen de crear comentarios
# *   en el lenguaje (en una línea, varias...).
# * - Crea una variable (y una constante si el lenguaje lo soporta).
# * - Crea variables representando todos los tipos de datos primitivos
# *   del lenguaje (cadenas de texto, enteros, booleanos...).
# * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
# *
# * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
# * debemos comenzar por el principio.
# */


# <--- PYTHON --->

# * - Crea un comentario en el código y coloca la URL del sitio web oficial del
# *   lenguaje de programación que has seleccionado.

#URL oficial: https://www.python.org/

############################################################
# * - Representa las diferentes sintaxis que existen de crear comentarios
# *   en el lenguaje (en una línea, varias...).

# Comentario de una línea

# Podemos seguir usando la almohadilla para hacer comentarios multilínea
"""o podemos usar comillas triples para comentarios multilínea,
pero éstos mismos no son considerados comentarios
si no cadenas de texto que no se asignan a ninguna variable,
por lo tanto son ignorados por la ejecución del programa"""

#############################################################
# * - Crea una variable (y una constante si el lenguaje lo soporta).

# Variable ejemplo:
color = "naranja"

# Constante ejemplo:
# Constantes declaradas por convención en MAYÚSCULAS, ya que Python no tiene soporte nativo para constantes.
PI = 3.14159
GRAVEDAD_TIERRA = 9.81
URL_API = "https://miweb.com"

# El lenguaje te permite cambiarlo, pero NO debes hacerlo:
# PI = 4.0  <- Esto es una mala práctica

# También podemos usar el módulo typing para declarar constantes con tipado estricto
from typing import Final

# Declaración con tipado estricto
MAX_CONEXIONES: Final = 5

# Si intentas hacer esto, tu editor te avisará que está mal:
MAX_CONEXIONES = 10 

###############################################################
# * - Crea variables representando todos los tipos de datos primitivos
# *   del lenguaje (cadenas de texto, enteros, booleanos...).

# Strings
nombre = "Juan"
# Integer
edad = 30
# Float
altura = 1.75
# Booleanos
es_estudiante = True
# Listas
frutas = ["manzana", "banana", "cereza"]
# Tuplas
coordenadas = (10.0, 20.0)
# Diccionarios
persona = {"nombre": "Ana", "edad": 25}
# Conjuntos
colores = {"rojo", "verde", "azul"}
# NoneType
valor_nulo = None

##############################################################
# * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print("¡Hola, Python!")