import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def crear_grafo():
    G = nx.Graph()
    
    conexiones = {
        ('CDMX', 'EdoMex'): 50,
        ('CDMX', 'Morelos'): 80,
        ('EdoMex', 'Puebla'): 120,
        ('Morelos', 'Guerrero'): 100,
        ('Puebla', 'Veracruz'): 150,
        ('Guerrero', 'Oaxaca'): 200,
        ('Oaxaca', 'Veracruz'): 250,
    }
    
    for (estado1, estado2), costo in conexiones.items():
        G.add_edge(estado1, estado2, weight=costo)
    
    return G

def costo_recorrido(G, recorrido):
    costo_total = 0
    for i in range(len(recorrido) - 1):
        if G.has_edge(recorrido[i], recorrido[i+1]):
            costo_total += G[recorrido[i]][recorrido[i+1]]['weight']
        else:
            return float('inf')  
    return costo_total

def encontrar_camino_hamiltoniano(G):
    estados = list(G.nodes)
    mejor_camino = None
    menor_costo = float('inf')
    
    for perm in permutations(estados):
        costo = costo_recorrido(G, perm)
        if costo < menor_costo:
            mejor_camino = perm
            menor_costo = costo
    
    return mejor_camino, menor_costo

def recorrido_con_repeticion(G):
    estados = list(G.nodes)
    recorrido = ['CDMX', 'EdoMex', 'Puebla', 'Veracruz', 'Oaxaca', 'Guerrero', 'Morelos', 'CDMX']  # Se repite CDMX
    return recorrido, costo_recorrido(G, recorrido)

def dibujar_grafo(G):
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(8,6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def main():
    G = crear_grafo()
    
    hamiltoniano, costo_hamiltoniano = encontrar_camino_hamiltoniano(G)
    if hamiltoniano:
        print(f"Recorrido sin repetir estados: {hamiltoniano}")
        print(f"Costo total: {costo_hamiltoniano}")
    else:
        print("No se encontró un camino hamiltoniano válido.")
    
    repetido, costo_repetido = recorrido_con_repeticion(G)
    print(f"Recorrido repitiendo un estado: {repetido}")
    print(f"Costo total: {costo_repetido}")
    
    dibujar_grafo(G)

if __name__ == "__main__":
    main()
