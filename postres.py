class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        
class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def insertar_ingrediente(self, nombre):
        nuevo = NodoIngrediente(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar_ingrediente(self, nombre):
        actual = self.cabeza
        previo = None
        while actual and actual.nombre != nombre:
            previo = actual
            actual = actual.siguiente
        if not actual:
            print(f"⚠️ Ingrediente '{nombre}' no encontrado.")
            return
        if not previo:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente
        print(f"✅ Ingrediente '{nombre}' eliminado.")

    def imprimir_ingredientes(self):
        actual = self.cabeza
        if not actual:
            print("❗ No hay ingredientes para este postre.")
            return
        while actual:
            print(f"- {actual.nombre}")
            actual = actual.siguiente
class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = ListaIngredientes()


class ListaPostres:
    def __init__(self):
        self.postres = []  

    def mostrar_todos_los_postres(self):
        if not self.postres:
            print("❗ No hay postres en la lista.")
            return
        print("\n🍰 Lista de postres disponibles:")
        for i, postre in enumerate(self.postres):
            print(f"{i + 1}. {postre.nombre}")

    def agregar_postre(self, nombre):
        nuevo_postre = Postre(nombre)
        for postre in self.postres:
            if postre.nombre == nombre:
                print(f"⚠️ El postre '{nombre}' ya existe.")
                return
        if not self.postres:
            self.postres.append(nuevo_postre)
        else:
            pos = 0
            while pos < len(self.postres) and self.postres[pos].nombre < nombre:
                pos += 1
            self.postres.insert(pos, nuevo_postre)
        print(f"✅ Postre '{nombre}' agregado y almacenado alfabéticamente.")

    def eliminar_postre(self, nombre):
        for i, postre in enumerate(self.postres):
            if postre.nombre == nombre:
                del self.postres[i]
                print(f"✅ Postre '{nombre}' eliminado correctamente.")
                return
        print(f"⚠️ El postre '{nombre}' no existe.")

    def imprimir_ingredientes_postre(self, nombre):
        for postre in self.postres:
            if postre.nombre == nombre:
                print(f"🍰 Ingredientes de '{nombre}':")
                postre.ingredientes.imprimir_ingredientes()
                return
        print(f"⚠️ El postre '{nombre}' no existe.")

    def insertar_ingredientes_postre(self, nombre_postre):
        for postre in self.postres:
            if postre.nombre == nombre_postre:
                print(f"🥄 Agregando ingredientes a '{nombre_postre}'...")
                while True:
                    nombre_ingrediente = input("➕ Escribe el nombre del ingrediente o escribe '2' para terminar: ").strip()
                    if nombre_ingrediente == "2":
                        print(f"✅ Ingredientes agregados a '{nombre_postre}'.")
                        break
                    elif nombre_ingrediente:
                        postre.ingredientes.insertar_ingrediente(nombre_ingrediente)
                        print(f"✅ Ingrediente '{nombre_ingrediente}' agregado.")
                return
        print(f"⚠️ El postre '{nombre_postre}' no existe.")

    def eliminar_ingrediente_postre(self, nombre_postre, nombre_ingrediente):
        for postre in self.postres:
            if postre.nombre == nombre_postre:
                postre.ingredientes.eliminar_ingrediente(nombre_ingrediente)
                return
        print(f"⚠️ El postre '{nombre_postre}' no existe.")

    def eliminar_duplicados_postres(self):
        nombres_vistos = set()
        postres_unicos = []
        for postre in self.postres:
            if postre.nombre not in nombres_vistos:
                nombres_vistos.add(postre.nombre)
                postres_unicos.append(postre)
        self.postres = postres_unicos
        print("✅ Se han eliminado los postres duplicados.")

def menu():
    mi_lista_postres = ListaPostres()

    while True:

        mi_lista_postres.mostrar_todos_los_postres()

        print("\n🍰 MENÚ DE POSTRES 🍰")
        print("1. Agregar un nuevo postre")
        print("2. Eliminar un postre")
        print("3. Mostrar ingredientes de un postre")
        print("4. Agregar ingredientes a un postre")
        print("5. Eliminar un ingrediente de un postre")
        print("6. Eliminar postres duplicados")
        print("7. Salir")

        opcion = input("👉 Elige una opción (1-7): ")

        if opcion == "1":
            nombre_postre = input("🍩 Nombre del nuevo postre: ").strip()
            mi_lista_postres.agregar_postre(nombre_postre)

        elif opcion == "2":
            nombre_postre = input("🗑️ Nombre del postre a eliminar: ").strip()
            mi_lista_postres.eliminar_postre(nombre_postre)

        elif opcion == "3":
            nombre_postre = input("🔍 Nombre del postre para ver ingredientes: ").strip()
            mi_lista_postres.imprimir_ingredientes_postre(nombre_postre)

        elif opcion == "4":
            nombre_postre = input("🍫 Nombre del postre para agregar ingredientes: ").strip()
            mi_lista_postres.insertar_ingredientes_postre(nombre_postre)

        elif opcion == "5":
            nombre_postre = input("🗑️ Nombre del postre para eliminar ingrediente: ").strip()
            nombre_ingrediente = input("❌ Nombre del ingrediente a eliminar: ").strip()
            mi_lista_postres.eliminar_ingrediente_postre(nombre_postre, nombre_ingrediente)

        elif opcion == "6":
            mi_lista_postres.eliminar_duplicados_postres()

        elif opcion == "7":
            print("👋 Saliendo del programa...")
            break

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
