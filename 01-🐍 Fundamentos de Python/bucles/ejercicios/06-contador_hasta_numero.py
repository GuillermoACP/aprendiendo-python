'''
✅ Ejercicio 1: Contador hasta un número

Escribe una función contar_hasta(n) que reciba un número entero positivo n y devuelva una lista con los números del 1 al n (inclusive), usando un bucle while.

📌 Ejemplo:

contar_hasta(5)
# → [1, 2, 3, 4, 5]
# '''

def contar_hasta(n):
    contador = 1
    lista = []
    while contador <= n:
        lista.append(contador)
        contador += 1
    return lista

print (contar_hasta(5))
'''
🎯 Pistas:

    Crea una variable contador que empiece en 1.
    Usa un while contador <= n: para repetir mientras el contador no supere a n.
    En cada vuelta, agrega el número a una lista con .append().
    No olvides aumentar el contador con contador += 1 dentro del ciclo.
'''