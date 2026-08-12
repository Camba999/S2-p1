for curso in range (4):
    curso = curso + 1
    total = 0
    for estudiante in range(6):
        estudiante = estudiante + 1
        print("1. Asistio -- 2. No asistio")
        asistencia = int(input(f"Ingrese la asistencia del estudiante {estudiante} del curso {curso}:"))
        if (asistencia == 0) or (asistencia == 1):
            total += asistencia
        else:
            print("Numero no valido")
            break
            
    print(f"Del curso {curso} solo asistieron {total} estudiantes de 6")
