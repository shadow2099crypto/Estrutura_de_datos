def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if str(lista[j]) < str(lista[min_idx]):
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

entrada = input("Ingresa letras, palabras o números separados por espacios: ")
elementos = entrada.split() 
seleccion(elementos)
print("Lista ordenada:", elementos)
