# ✅ Ejercicio 1: Verificación de Acceso
# Enunciado:
# Escribe una función puede_entrar(nombre, edad) que reciba un nombre y una edad, y devuelva:
#     "Bienvenido" si:
#         El nombre no está en la lista de personas prohibidas y
#         La edad está entre 18 y 60 (inclusive).
#     "Acceso denegado" en cualquier otro caso.



# Lista de personas prohibidas
prohibidos = ['Carlos', 'Lucía', 'Mariana']

tu_nombre = input('Escribe tu nombre: ')
tu_edad = int(input('Escribe tu edad: '))

def puede_entrar(nombre, edad):
    if nombre not in prohibidos and 18 <= edad <= 60:
        validacion = ' Bienvenido'
    else:
        validacion = 'Acesso Denegado'
    return (validacion)

print(puede_entrar(tu_nombre, tu_edad))




# Pistas:
#     Usa in para verificar si el nombre está en prohibidos.
#     Usa and para combinar condiciones.
#     Usa not in para negar la pertenencia.