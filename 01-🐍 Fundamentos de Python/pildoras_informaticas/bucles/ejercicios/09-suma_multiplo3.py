'''
🧠 Ejercicio 9: Suma de múltiplos de 3

📝 Instrucción:
Crea un programa en Python que pida al usuario un número entero positivo n y sume todos los múltiplos de 3 desde 1 hasta n. Al final, debe mostrar el total acumulado.

📌 Ejemplo:
Introduce un número: 10  
La suma de los múltiplos de 3 desde 1 hasta 10 es: 18

    (Porque los múltiplos de 3 hasta el 10 son: 3, 6, 9 → 3 + 6 + 9 = 18)
'''

def multiplo_tres(n):
    acumuladora = 0
    x = range(1, n+1)
    for numero in x:
        if numero % 3 == 0:
            acumuladora += numero

    return acumuladora

print(multiplo_tres(10))


'''
💡 Pistas (si lo necesitas):
    Usa range(1, n+1) para recorrer desde 1 hasta n.
    Verifica si el número actual es divisible entre 3 usando if numero % 3 == 0.
    Usa una variable acumuladora para ir sumando.
'''