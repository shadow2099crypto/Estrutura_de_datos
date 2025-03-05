class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, item):
        self.elementos.append(item)
        print(f"Elemento '{item}' apilado")
    
    def desapilar(self):
        if self.esta_vacia():
            return "La pila está vacía"
        return self.elementos.pop()
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def cima(self):
        if self.esta_vacia():
            return "No hay elementos"
        return self.elementos[-1]
    
    def mostrar(self):
        if self.esta_vacia():
            print("Pila vacía")
        else:
            print("Elementos en la pila:")
            for elemento in reversed(self.elementos):
                print(f"| {elemento:^5} |")

def menu():
    print("\nMENÚ DE PILA")
    print("1. Apilar elemento")
    print("2. Desapilar elemento")
    print("3. Ver cima")
    print("4. Mostrar pila")
    print("5. Salir")

mi_pila = Pila()

while True:
    menu()
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        elemento = input("Ingresa el elemento a apilar: ")
        mi_pila.apilar(elemento)
    elif opcion == "2":
        resultado = mi_pila.desapilar()
        print(f"Elemento desapilado: {resultado}")
    elif opcion == "3":
        print(f"Elemento en la cima: {mi_pila.cima()}")
    elif opcion == "4":
        mi_pila.mostrar()
    elif opcion == "5":
        print("¡Adiós!")
        break
    else:
        print("Opción inválida. Intenta nuevamente")