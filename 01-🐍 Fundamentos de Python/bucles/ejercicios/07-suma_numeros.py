'''
✅ Ejercicio 2: Suma de números hasta cero

Escribe una función suma_hasta_cero() que pida al usuario ingresar números uno por uno (usando input()), y los vaya sumando hasta que se ingrese un 0. Cuando eso ocurra, debe devolver la suma total.

📌 Ejemplo (simulación):

Ingresa un número: 3  
Ingresa un número: 5  
Ingresa un número: -2  
Ingresa un número: 0  
# → Resultado: 6
'''

def suma_hasta_cero():
    suma_total = 0
    numero = int(input('Ingresa un número: '))
    while numero != 0:
        suma_total = suma_total + numero
        numero = int(input('Ingresa un número: '))
    return suma_total

print(suma_hasta_cero())        

'''
🎯 Pistas:

    Usa un while para repetir mientras el número no sea 0.
    Convierte el input a entero: numero = int(input(...))
    Lleva una suma acumulada en una variable.
    Cuando se ingrese 0, el ciclo termina y se devuelve la suma.
'''
