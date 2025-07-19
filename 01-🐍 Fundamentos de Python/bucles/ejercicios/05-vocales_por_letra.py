'''
✅ Ejercicio 5: Contar cuántas veces aparece cada letra
🧩 Enunciado:
Escribe una función contar_letras(texto) que reciba una cadena y devuelva un diccionario donde cada letra (excepto espacios) sea una clave, y su valor sea la cantidad de veces que aparece en el texto.

contar_letras("hola mundo")
# → {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
'''

ejemplo = ("hola mundo")
def contar_letras(mensaje):
    frecuencias = {} 
    for letra in mensaje:   
        if letra == ' ':
            continue
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias

print(contar_letras(ejemplo))     

'''
🧠 Pistas para resolverlo:
    Crea un diccionario vacío: frecuencias = {}
    Usa un for para recorrer cada letra del texto.
    Ignora los espacios: if letra != ' ':
    Si la letra ya está en el diccionario, aumenta su valor en 1.
    Si no está, agrégala con valor 1.
    Devuelve el diccionario al final.
'''