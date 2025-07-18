print('Programa de Evalucion de notas del alumno')

nota_alumno = input('Agrega la nota del alumno: ')

def evaluacion (nota):
    valoracion = 'Aprobado'
    if nota < 5:
        valoracion = 'Reprobado'
    return valoracion

print (evaluacion(int(nota_alumno)))

