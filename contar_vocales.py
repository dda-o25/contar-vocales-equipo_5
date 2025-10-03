"""
El propósito de este programa es que dada una palabra, el programa cuente la cantidad de letras en la palabra
Eduardo Caleb Castillo Llanas
Daniel Maldonado Delgado
Larisa Carolina Alvarez Gonzales
Ximena Castro Flores
03/Oct/25
"""

# Declaraciones
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
contador = 0
# Entradas
frase = input("Introduzca una frase: ")

# Proceso

for letra in frase:
    if letra in vocales:
        contador += 1
print(f"La palabra '{frase}' tiene {contador} vocales.")
