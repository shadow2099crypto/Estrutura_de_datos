import random

def crear_tabla_calificaciones(num_alumnos, num_materias):
    tabla = {}
    materias = [f"materia{i+1}" for i in range(num_materias)]
    
    for i in range(num_alumnos):
        alumno = f"alumno{i+1}"
        tabla[alumno] = {}
        for materia in materias:
            tabla[alumno][materia] = random.randint(0, 100)
    
    return tabla, materias

def buscar_alumno_materia(tabla, alumno, materia):
    if alumno in tabla and materia in tabla[alumno]:
        return f"La calificación de {alumno} en {materia} es: {tabla[alumno][materia]}"
    else:
        return "No se encontró el alumno o la materia especificada"

def mostrar_tabla(tabla, materias):
    print("\nTabla de Calificaciones:")
    print("Alumno", end="\t")
    for materia in materias:
        print(f"{materia}", end="\t")
    print()
    
    for alumno in tabla:
        print(f"{alumno}", end="\t")
        for materia in materias:
            print(f"{tabla[alumno][materia]}", end="\t")
        print()

def main():
    try:
        num_alumnos = int(input("Ingrese el número de alumnos: "))
        num_materias = int(input("Ingrese el número de materias: "))
        
        if num_alumnos <= 0 or num_materias <= 0:
            print("Por favor ingrese números positivos")
            return
        
        tabla, materias = crear_tabla_calificaciones(num_alumnos, num_materias)
        mostrar_tabla(tabla, materias)
        
        while True:
            print("\n1. Buscar calificación")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                alumno = input("Ingrese el número de alumno (ejemplo: alumno1): ")
                print("Materias disponibles:", ", ".join(materias))
                materia = input("Ingrese el nombre de la materia: ")
                print(buscar_alumno_materia(tabla, alumno, materia))
            elif opcion == "2":
                break
            else:
                print("Opción no válida")
    
    except ValueError:
        print("Por favor ingrese números válidos")

if __name__ == "__main__":
    main()