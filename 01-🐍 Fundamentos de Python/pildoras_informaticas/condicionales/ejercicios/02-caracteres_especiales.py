# ✅ Ejercicio 2: Revisión de Caracteres Especiales
# Enunciado:
# Escribe una función tiene_caracter_especial(cadena) que devuelva True si la cadena contiene al menos uno de estos caracteres especiales: @, #, o !. Si no, devuelve False.

contraseña = input('Crea tu Contraseña: ')

def tiene_caracter_especial(cadena):
    if '@' in cadena or '#' in cadena or '!' in cadena:
        return True
    else:
        return False

print(tiene_caracter_especial(contraseña))

#Version Compacta IA:

# def tiene_caracter_especial(cadena):
#     return any(c in cadena for c in ['@', '#', '!'])

# contraseña = input('Crea tu Contraseña: ')
# print(tiene_caracter_especial(contraseña))


# Pistas:
#     Puedes usar in varias veces combinado con or.
#     O puedes hacer una solución más compacta con bucles y sets si te animas a retarlo más.