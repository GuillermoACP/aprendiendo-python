'''
✅ Ejercicio 4: Palabras que contienen una vocal específica

Escribe una función palabras_con_vocal(frase, vocal) que reciba una frase y una vocal (por ejemplo 'a'), y devuelva una lista con las palabras que contienen esa vocal.
Ejemplo:

palabras_con_vocal("hola mundo esto es python", "o")
# → ['hola', 'mundo', 'python']
'''

ejemplo = ("hola mundo esto es python")

def palabras_con_vocal(frase, vocal):
    resultado = []
    palabras = frase.split()
    for palabra_individual in palabras:
        if vocal in palabra_individual:
            resultado.append(palabra_individual)
    
    return resultado

print(palabras_con_vocal(ejemplo, 'o'))

'''
Pistas:
    Usa .split() para dividir la frase.
    Usa if vocal in palabra para revisar si la palabra tiene la vocal.
    Recolecta las que cumplen con un .append() en una lista.
'''