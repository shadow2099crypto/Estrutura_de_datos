class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad  
        self.pila = []  
        self.tope = 0  

    def insertar(self, elemento):
        if self.tope < self.capacidad:  
            self.pila.append(elemento)
            self.tope += 1
            print(f"Insertado: {elemento} | PILA: {self.pila} | TOPE: {self.tope}")
        else:
            print("Error: Desbordamiento (Overflow), la pila está llena.")

    def eliminar(self):
        if self.tope > 0:  
            elemento = self.pila.pop()
            self.tope -= 1
            print(f"Eliminado: {elemento} | PILA: {self.pila} | TOPE: {self.tope}")
        else:
            print("Error: Subdesbordamiento (Underflow), la pila está vacía.")

pila = Pila(8)

pila.insertar('X')  
pila.insertar('Y')  
pila.eliminar()    
pila.eliminar()     
pila.eliminar()     
pila.insertar('V')  
pila.insertar('W')  
pila.eliminar()     
pila.insertar('R')  