print('Programa de Evalucion de notas del alumno')
nota_alumno = int(input('Agrega la nota del alumno: '))

def evaluacion (nota):
    if nota_alumno < 5:
        valoracion = 'Reprobado'
    else:
        valoracion = 'Aprobado'

    return valoracion

print (evaluacion(nota_alumno))

