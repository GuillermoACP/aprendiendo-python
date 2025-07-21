'''
✅ Ejercicio 1: Contar vocales
Enunciado:
Escribe una función contar_vocales(cadena) que reciba una cadena de texto y devuelva cuántas vocales (a, e, i, o, u) contiene.
'''

nombre = input('Intruduce tu nombre: ')

def contar_vocales(cadena):
    contador = 0
    for i in cadena:
        if i in 'aeiou':
            contador = contador+1

    return contador

print (contar_vocales(nombre))

'''
Pistas:
    Usa un for para recorrer cada letra de la cadena.
    Compara si cada letra está en un conjunto o lista de vocales.
    Suma un contador cada vez que encuentres una.
'''