
class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

def mover_disco(origen, destino, nom_origen, nom_destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} de {nom_origen} a {nom_destino}")

def movimiento_legal(pila1, pila2, nom1, nom2):

    if pila1.esta_vacia():
        mover_disco(pila2, pila1, nom2, nom1)
    elif pila2.esta_vacia():
        mover_disco(pila1, pila2, nom1, nom2)
    else:
        top1 = pila1.ver_tope()
        top2 = pila2.ver_tope()
        if top1 < top2:
            mover_disco(pila1, pila2, nom1, nom2)
        else:
            mover_disco(pila2, pila1, nom2, nom1)

def hanoi_iterativo(n, origen, auxiliar, destino, nom_origen, nom_auxiliar, nom_destino):
    total_movimientos = 2**n - 1

    if n % 2 == 0:
        auxiliar, destino = destino, auxiliar
        nom_auxiliar, nom_destino = nom_destino, nom_auxiliar

    for i in range(1, total_movimientos + 1):
        if i % 3 == 1:
            movimiento_legal(origen, destino, nom_origen, nom_destino)
        elif i % 3 == 2:
            movimiento_legal(origen, auxiliar, nom_origen, nom_auxiliar)
        elif i % 3 == 0:
            movimiento_legal(auxiliar, destino, nom_auxiliar, nom_destino)

def main():
    torreA = Pila()
    torreB = Pila()
    torreC = Pila()

    n = 3  

    for disco in range(n, 0, -1):
        torreA.apilar(disco)

    print("Resolviendo Torres de Hanoi para 3 discos:")
    hanoi_iterativo(n, torreA, torreB, torreC, "A", "B", "C")

if __name__ == "__main__":
    main()

