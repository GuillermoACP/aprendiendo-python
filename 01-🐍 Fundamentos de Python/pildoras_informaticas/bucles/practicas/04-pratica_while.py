import math

print('Programa de Cálculo de Raíz Cuadrada')

intentos = 0
numero = int(input('Introduce el número: '))

while numero < 0 and intentos < 2:
    print('No se aceptan números negativos')
    intentos += 1
    numero = int(input('Introduce el número: '))

if intentos == 2:
    print('Demasiados intentos. Finalizado')
else:
    def raiz_cuadra(n):
        solucion = math.sqrt(n)
        return solucion

    resultado = raiz_cuadra(numero)
    print(f'La raíz cuadrada de {numero} es {resultado}')
