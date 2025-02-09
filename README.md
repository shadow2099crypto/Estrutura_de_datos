Arreglo (Python)

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
Arreglo de ventas (Python and Java)
Este programa hecho en Python y Java con ligeras modificaciones simula el registro y manejo de ventas por departamento durante un año. Está compuesto por una matriz de ventas que tiene 12 filas (representando los meses del año) y 3 columnas (representando 3 departamentos: "Ropa", "Deportes" y "Juguetería"). Cada celda en la matriz almacena las ventas realizadas en ese mes y departamento específicos, y permite agregar, eliminar o consultar las ventas registradas. Dado que su objetivo de este código fue que el usuario proporcione la información de manera más ágil y crear la tabla más rápido en vez de escribirlo a mano haciendo que tarde más el desarrollo de este, y en esta ocasión es en base a un menú, siempre con el mismo objetivo de proporcionarlo como tabla.
 Métodos: 
• Matriz de ventas: El programa define una matriz de 12 filas y 3 columnas con valores vacíos inicialmente.
• insertar_venta(): Permite al usuario ingresar el monto de una venta en un mes y departamento específicos. El monto se agrega a la lista de ventas en la celda correspondiente. 
• buscar_venta(): Muestra las ventas registradas en un mes y departamento seleccionados. Si no hay ventas, indica que la celda está vacía. 
• eliminar_venta(): Elimina todas las ventas de un mes y departamento específicos, vaciando la celda de ventas. 
• mostrar_tabla(): Muestra la matriz de ventas, solo mostrando los meses y departamentos con ventas registradas. Si no hay ventas en alguna celda, esa celda queda vacía. 
Menú: 
El programa ofrece un menú donde el usuario puede: 1. insertar 2. buscar 3. eliminar ventas 4. mostrar la tabla de ventas. La matriz se actualiza dinámicamente según las acciones del usuario, además como dato extra si se busca agregar otra cantidad en el mismo mes puede hacer que le dé a la opción 1, buscar el mismo mes que desea y agregar el otro departamento agregando la cantidad para luego ir a “mostrar la tabla” se refleje ambas opciones ya seleccionadas.

Arreglo(Java)
                                                                                                                                                                              
    import java.util.Scanner;
    public class Arreglo {

    static String[][] ventas = new String[12][3];
    static String[] meses = {
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    };
    static String[] departamentos = {"Ropa", "Deportes", "Juguetería"};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Insertar venta");
            System.out.println("2. Buscar venta");
            System.out.println("3. Eliminar venta");
            System.out.println("4. Mostrar tabla de ventas");
            System.out.println("5. Salir");
            System.out.print("Selecciona una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine(); 

            if (opcion == 1) {
                insertarVenta(scanner);
            } else if (opcion == 2) {
                buscarVenta(scanner);
            } else if (opcion == 3) {
                eliminarVenta(scanner);
            } else if (opcion == 4) {
                mostrarTabla();
            } else if (opcion == 5) {
                System.out.println("¡Adiós!");
                break;
            } else {
                System.out.println("Opción no válida. Intenta de nuevo.");
            }
        }
        scanner.close();
    }

    public static void insertarVenta(Scanner scanner) {
        System.out.println("\nInsertar una venta:");
        
        for (int i = 0; i < meses.length; i++) {
            System.out.println((i + 1) + ". " + meses[i]);
        }
        System.out.print("Selecciona un mes (1-12): ");
        int mesIndex = scanner.nextInt() - 1;
        
        for (int i = 0; i < departamentos.length; i++) {
            System.out.println((i + 1) + ". " + departamentos[i]);
        }
        System.out.print("Selecciona un departamento (1-3): ");
        int depIndex = scanner.nextInt() - 1;
        
        scanner.nextLine(); 
        System.out.print("Ingresa el monto de la venta: ");
        String monto = scanner.nextLine();
        
        ventas[mesIndex][depIndex] = monto;
        System.out.println("Venta agregada correctamente.");
    }

    public static void buscarVenta(Scanner scanner) {
        System.out.println("\nBuscar una venta:");
        
        for (int i = 0; i < meses.length; i++) {
            System.out.println((i + 1) + ". " + meses[i]);
        }
        System.out.print("Selecciona un mes (1-12): ");
        int mesIndex = scanner.nextInt() - 1;
        
        for (int i = 0; i < departamentos.length; i++) {
            System.out.println((i + 1) + ". " + departamentos[i]);
        }
        System.out.print("Selecciona un departamento (1-3): ");
        int depIndex = scanner.nextInt() - 1;
        
        if (!ventas[mesIndex][depIndex].isEmpty()) {
            System.out.println("Venta encontrada: " + ventas[mesIndex][depIndex]);
        } else {
            System.out.println("No hay venta registrada en esa posición.");
        }
    }

    public static void eliminarVenta(Scanner scanner) {
        System.out.println("\nEliminar una venta:");
        
        for (int i = 0; i < meses.length; i++) {
            System.out.println((i + 1) + ". " + meses[i]);
        }
        System.out.print("Selecciona un mes (1-12): ");
        int mesIndex = scanner.nextInt() - 1;
        
        for (int i = 0; i < departamentos.length; i++) {
            System.out.println((i + 1) + ". " + departamentos[i]);
        }
        System.out.print("Selecciona un departamento (1-3): ");
        int depIndex = scanner.nextInt() - 1;
        
        ventas[mesIndex][depIndex] = "";
        System.out.println("Venta eliminada correctamente.");
    }

    public static void mostrarTabla() {
        System.out.println("\nTabla de ventas:");
        System.out.printf("%-12s %-12s %-12s %-12s\n", "", departamentos[0], departamentos[1], departamentos[2]);
        
        for (int i = 0; i < meses.length; i++) {
            System.out.printf("%-12s %-12s %-12s %-12s\n", meses[i], ventas[i][0], ventas[i][1], ventas[i][2]);
        }
    }
    }

Continuando con este programa ahora en Java administra un registro de ventas organizadas por mes y departamento así que se implementaron estos métodos:
1.	main():
o	Muestra un menú interactivo con opciones para insertar, buscar, eliminar ventas o mostrar la tabla.
o	Utiliza un bucle while para mantener el menú activo hasta que el usuario seleccione "Salir".
o	Llama a los métodos correspondientes según la opción elegida.

2.	insertarVenta(Scanner scanner):
o	Permite al usuario seleccionar un mes y un departamento.
o	Solicita el monto de la venta y lo almacena en la matriz ventas en la posición correspondiente.

3.	buscarVenta(Scanner scanner):
o	Permite al usuario seleccionar un mes y un departamento.
o	Muestra el monto registrado en esa posición si existe; de lo contrario, indica que no hay venta registrada.

4.	eliminarVenta(Scanner scanner):
o	Permite al usuario seleccionar un mes y un departamento.
o	Borra la venta en esa posición asignando una cadena vacía "".

5.	mostrarTabla():
o	Muestra la tabla completa de ventas con los nombres de los meses y departamentos organizados en formato tabular.
