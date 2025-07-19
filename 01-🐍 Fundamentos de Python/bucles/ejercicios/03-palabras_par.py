'''
✅ Ejercicio 3: Palabras con longitud par

Enunciado:
Escribe una función palabras_pares(frase) que reciba una cadena con varias palabras y devuelva una lista con solo las palabras que tienen una cantidad par de letras.

Ejemplo:

palabras_pares("hola mundo esto es python")  
# → ['hola', 'mundo', 'es']
'''
ejemplo = ("hola mundo esto es python")

def palabras_pares(frase):
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        if len(palabra) % 2 == 0:
            resultado.append(palabra)
    return resultado

print(palabras_pares(ejemplo))
'''
Pistas:
    Usa frase.split() para convertir la cadena en una lista de palabras.
    Recorre esa lista con un for.
    Usa len(palabra) % 2 == 0 para saber si la palabra tiene longitud par.
    Agrega con .append las que cumplen la condición a una nueva lista.
'''