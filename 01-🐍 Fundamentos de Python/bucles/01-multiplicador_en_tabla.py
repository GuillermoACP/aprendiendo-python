print("Tabla de multiplicar dado un numero")

num = input()
print(f'Tabla del {num}')
for i in range(0,11):
    resultado = int(num) * i
    print(f'{num} X {i} = {resultado}')

