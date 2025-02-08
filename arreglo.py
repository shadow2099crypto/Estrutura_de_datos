ventas = [[[] for _ in range(3)] for _ in range(12)]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
departamentos = ["Ropa", "Deportes", "Juguetería"]

def insertar_venta():
    print("\nInsertar una venta:")
    for i, mes in enumerate(meses):
        print(f"{i + 1}. {mes}")
    mes_index = int(input("Selecciona un mes (1-12): ")) - 1
    for i, dept in enumerate(departamentos):
        print(f"{i + 1}. {dept}")
    dep_index = int(input("Selecciona un departamento (1-3): ")) - 1
    monto = input("Ingresa el monto de la venta: ")
    
    ventas[mes_index][dep_index].append(monto)
    print("Venta agregada correctamente.")

def buscar_venta():
    print("\nBuscar una venta:")
    for i, mes in enumerate(meses):
        print(f"{i + 1}. {mes}")
    mes_index = int(input("Selecciona un mes (1-12): ")) - 1
    for i, dept in enumerate(departamentos):
        print(f"{i + 1}. {dept}")
    dep_index = int(input("Selecciona un departamento (1-3): ")) - 1
    if ventas[mes_index][dep_index]:
        print("Ventas encontradas:", ", ".join(ventas[mes_index][dep_index]))
    else:
        print("No hay ventas registradas en esa posición.")

def eliminar_venta():
    print("\nEliminar ventas:")
    for i, mes in enumerate(meses):
        print(f"{i + 1}. {mes}")
    mes_index = int(input("Selecciona un mes (1-12): ")) - 1
    for i, dept in enumerate(departamentos):
        print(f"{i + 1}. {dept}")
    dep_index = int(input("Selecciona un departamento (1-3): ")) - 1
    ventas[mes_index][dep_index] = []
    print("Ventas eliminadas correctamente.")

def mostrar_tabla():
    print("\nTabla de ventas:")
    print("{:<12} {:<12} {:<12} {:<12}".format("", *departamentos))
    for i, mes in enumerate(meses):
        if any(ventas[i][j] for j in range(len(departamentos))):
            fila = []
            for j in range(len(departamentos)):
                if ventas[i][j]:
                    fila.append(", ".join(ventas[i][j]))
                else:
                    fila.append("")
            print("{:<12} {:<12} {:<12} {:<12}".format(mes, fila[0], fila[1], fila[2]))

while True:
    print("\n--- Menú ---")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar tabla de ventas")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        insertar_venta()
    elif opcion == "2":
        buscar_venta()
    elif opcion == "3":
        eliminar_venta()
    elif opcion == "4":
        mostrar_tabla()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
