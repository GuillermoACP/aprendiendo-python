print('Las Primeras 10 Tablas de Multiplicas')

for i in range(1,11):
    print('------------------------------')
    print(f'Tabla de Multiplicar del {i}')
    print()    
    for j in range(1,11):
        resultado = int(i * j)
        print (f'        {i} X {j} = {resultado}')
    print('------------------------------')
    print()