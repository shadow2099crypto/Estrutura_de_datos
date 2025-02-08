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
