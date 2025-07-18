print ('Verificacion de edad')

edad_usuario = int(input('Introduce tu edad: '))

def usuario (edad):
    if edad_usuario > 18:
        validacion ='Bienvenido!'
        if edad_usuario > 120:
            validacion = 'Edad Incorrecta'
    else: 
        validacion = 'Acesso Denegado'

    return validacion.upper()

print (usuario (edad_usuario))
    
    
