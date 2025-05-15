def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  
    return -1  


entrada = input("Escribe una lista de números separados por coma: ")

numeros = [int(x.strip()) for x in entrada.split(",")]

buscar = int(input("¿Qué número quieres buscar en la lista?: "))

resultado = busqueda_secuencial(numeros, buscar)

if resultado != -1:
    print(f"✅ Número {buscar} encontrado en la posición {resultado}")
else:
    print("❌ Número no encontrado en la lista")
