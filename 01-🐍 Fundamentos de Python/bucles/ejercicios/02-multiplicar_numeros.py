'''
✅ Ejercicio 2: Multiplicar todos los números
Enunciado:
Escribe una función producto_total(lista_numeros) que reciba una lista de números y devuelva el resultado de multiplicarlos todos.
Ejemplo:

producto_total([2, 3, 4]) → 24
'''
productos=[2,4,5]

def producto_total(lista_numeros):
    producto = 1
    for i in lista_numeros:
       producto = producto * i
    return producto

print(producto_total(productos))


'''
Pistas:
    Crea una variable producto = 1 al inicio.
    Usa un for para recorrer la lista y multiplicar cada número por producto.
'''