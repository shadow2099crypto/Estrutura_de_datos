import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo = heapq.heappop(cola)
        for vecino, peso in grafo[nodo]:
            nueva_dist = distancia_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))
    return distancias


def floyd(grafo):
    nodos = list(grafo.keys())
    dist = {i: {j: float('inf') for j in nodos} for i in nodos}

    for nodo in nodos:
        dist[nodo][nodo] = 0
    for u in grafo:
        for v, peso in grafo[u]:
            dist[u][v] = peso

    for k in nodos:
        for i in nodos:
            for j in nodos:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def warshall(grafo):
    nodos = list(grafo.keys())
    alcanzable = {i: {j: False for j in nodos} for i in nodos}

    for nodo in nodos:
        alcanzable[nodo][nodo] = True
    for u in grafo:
        for v, _ in grafo[u]:
            alcanzable[u][v] = True

    for k in nodos:
        for i in nodos:
            for j in nodos:
                if not alcanzable[i][j]:
                    alcanzable[i][j] = alcanzable[i][k] and alcanzable[k][j]

    return alcanzable

class UnionFind:
    def __init__(self, vertices):
        self.padre = {v: v for v in vertices}

    def encontrar(self, v):
        if self.padre[v] != v:
            self.padre[v] = self.encontrar(self.padre[v])
        return self.padre[v]

    def unir(self, u, v):
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)
        if raiz_u != raiz_v:
            self.padre[raiz_v] = raiz_u
            return True
        return False

def kruskal(grafo):
    aristas = []
    for u in grafo:
        for v, peso in grafo[u]:
            aristas.append((peso, u, v))
    aristas.sort()

    uf = UnionFind(grafo.keys())
    mst = []
    for peso, u, v in aristas:
        if uf.unir(u, v):
            mst.append((u, v, peso))

    return mst

if __name__ == "__main__":
    grafo_dijkstra = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    print("\nDijkstra desde A:")
    print(dijkstra(grafo_dijkstra, 'A'))

    grafo_floyd = {
        'A': [('B', 3), ('C', 8)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': [('A', 2)]
    }
    print("\nFloyd:")
    resultado_floyd = floyd(grafo_floyd)
    for fila in resultado_floyd:
        print(fila, resultado_floyd[fila])

    print("\nWarshall:")
    resultado_warshall = warshall(grafo_floyd)
    for fila in resultado_warshall:
        print(fila, resultado_warshall[fila])

    grafo_kruskal = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 2)],
        'D': [('B', 4), ('C', 2)]
    }
    print("\nÁrbol de Expansión Mínima (Kruskal):")
    print(kruskal(grafo_kruskal))
