'''
🧠 Ejercicio: Cifrado por desplazamiento (Cifrado César)

Escribe una función llamada cesar_cifrado(texto, desplazamiento) que reciba un texto (solo letras minúsculas y espacios) y un número entero desplazamiento.

La función debe devolver el texto cifrado utilizando un cifrado César, es decir, desplazando cada letra del alfabeto tantas posiciones como indique desplazamiento.

    Las letras deben rotar: si te pasas de la "z", empieza desde la "a" otra vez.
    Los espacios deben mantenerse igual.
    No uses funciones especiales como ord() ni chr() si aún no las has visto. Puedes usar una lista de letras.

Ejemplo:

cesar_cifrado("hola mundo", 2)  # devuelve: "jqnc owpfq"
'''

def cesar_cifrado(texto, desplazamiento):
    letras = list("abcdefghijklmnopqrstuvwxyz")
    resultado = []

    for caracter in texto:
        if caracter == ' ':
            resultado.append(' ')
        else:
            indice_actual = letras.index(caracter)            # Encuentra la posición del caracter
            nuevo_indice = (indice_actual + desplazamiento) % 26  # Aplica el desplazamiento con rotación
            nueva_letra = letras[nuevo_indice]               # Obtiene la nueva letra cifrada
            resultado.append(nueva_letra)                    # Agrega la letra cifrada a la lista

    return ''.join(resultado)  # Une todas las letras en una sola cadena
'''
🔧 Pistas:

    Puedes crear una lista con todas las letras:

letras = list("abcdefghijklmnopqrstuvwxyz")

Recorre cada letra del texto con un bucle (for).
Usa un bucle para encontrar el índice actual de cada letra y luego sumar el desplazamiento.
Si el índice se pasa de 25, vuelve al principio (usa el operador % para eso).
Une las letras cifradas en un nuevo string.
'''