
# Sistema de Calificaciones de Estudiantes
# Introduccion a la Programacion - Capitulo IX

calificaciones = [85, 67, 92, 74, 58]

print("SISTEMA DE CALIFICACIONES")
print("Calificaciones iniciales:", calificaciones)

# Acceso a un elemento mediante su indice
print("Primera calificacion:", calificaciones[0])

# Recorrido y conteo de aprobados y reprobados
aprobados = 0
reprobados = 0

for nota in calificaciones:
    print("Calificacion:", nota)
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

# Calculos del vector
promedio = sum(calificaciones) / len(calificaciones)
nota_mayor = max(calificaciones)
nota_menor = min(calificaciones)

print("Promedio:", round(promedio, 2))
print("Nota mas alta:", nota_mayor)
print("Nota mas baja:", nota_menor)
print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", reprobados)

# Modificacion de un elemento usando su indice
print("Vamos a modificar la calificacion en el indice 1.")
nueva_nota = int(input("Escriba la nueva calificacion (0 a 100): "))

if 0 <= nueva_nota <= 100:
    calificaciones[1] = nueva_nota
    print("Vector actualizado:", calificaciones)
    nuevo_promedio = sum(calificaciones) / len(calificaciones)
    print("Nuevo promedio:", round(nuevo_promedio, 2))
else:
    print("La calificacion debe estar entre 0 y 100.")
    print("El vector no fue modificado.")
