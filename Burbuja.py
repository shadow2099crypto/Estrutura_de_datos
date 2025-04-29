def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

entrada = input("Ingresa letras o palabras separadas por espacios: ")
elementos = entrada.split()  

burbuja(elementos)
print("Lista ordenada:", elementos)
