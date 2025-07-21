valido = False
email = input('Introduce tu Email: ')

for i in range(len(email)):
    if email [i] == "@":
        valido = True
 
if valido:
    print('Email Correcto')
else:
    print('Email incorrecto')