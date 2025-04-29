def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

entrada = input("Ingresa letras o palabras separadas por espacios: ")
elementos = entrada.split()  

insercion(elementos)
print("Lista ordenada:", elementos)

