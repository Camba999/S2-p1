for aula in range(4):
    suma = 0
    aula = aula + 1
    for estudiante in range(5):
        estudiante = estudiante + 1
        nota = float(input(f"Ingrese nota del estudiante {estudiante} del aula {aula}:"))
        suma += nota
        promedio = suma/5
    print(f"El promedio del aula {aula}: {promedio}")
