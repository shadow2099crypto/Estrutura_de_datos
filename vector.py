import random

def llenar_vector(longitud):
    return [random.randint(-100, 100) for _ in range(longitud)]

def sumar_vectores(a, b):
    return [a[i] + b[i] for i in range(len(a))]

def restar_vectores(a, b):
    return [b[i] - a[i] for i in range(len(a))]

def mostrar_vector(vector):
    print("Vector:", vector)

def main():
    vector_a = []
    vector_b = []
    vector_c = None
    longitud = int(input("Ingrese la longitud de los vectores: "))
    
    while True:
        print("\nMenú:")
        print("1. Llenar Vector A de manera aleatoria")
        print("2. Llenar Vector B de manera aleatoria")
        print("3. Realizar C = A + B")
        print("4. Realizar C = B - A")
        print("5. Mostrar un vector")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            vector_a = llenar_vector(longitud)
            print("Vector A llenado correctamente.")
        elif opcion == "2":
            vector_b = llenar_vector(longitud)
            print("Vector B llenado correctamente.")
        elif opcion == "3":
            if vector_a and vector_b:
                vector_c = sumar_vectores(vector_a, vector_b)
                print("Operación realizada: C = A + B")
            else:
                print("Error: Primero debe llenar los vectores A y B.")
        elif opcion == "4":
            if vector_a and vector_b:
                vector_c = restar_vectores(vector_a, vector_b)
                print("Operación realizada: C = B - A")
            else:
                print("Error: Primero debe llenar los vectores A y B.")
        elif opcion == "5":
            print("Elija qué vector desea mostrar (A, B o C): ")
            seleccion = input().upper()
            if seleccion == "A":
                mostrar_vector(vector_a)
            elif seleccion == "B":
                mostrar_vector(vector_b)
            elif seleccion == "C":
                if vector_c is not None:
                    mostrar_vector(vector_c)
                else:
                    print("Error: El vector C no ha sido calculado aún.")
            else:
                print("Opción no válida.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()