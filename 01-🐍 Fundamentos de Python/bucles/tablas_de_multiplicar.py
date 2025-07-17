#Ejercicio 1: "Patron numerico"

#for i in range(1, 10):
#    print(str(i) * 1)


#Ejercicio 2: "Tabla de multiplicar dado un numero"

# num = input()
# print(f'Tabla del {num}')
# for i in range(0,11):
#     resultado = int(num) * i
#     print(f'{num} X {i} = {resultado}')


#Ejercicio 3: "Las 10 Primeras Tablas"

for i in range(1,11):
    print('------------------------------')
    print(f'Tabla de Multiplicar del {i}')
    print()    
    for j in range(1,11):
        resultado = int(i * j)
        print (f'        {i} X {j} = {resultado}')
    print('------------------------------')
    print()