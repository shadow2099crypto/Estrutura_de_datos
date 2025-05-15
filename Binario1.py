def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

palabras = ["abeja", "ballena", "cabra", "delfín", "elefante", "foca", "jirafa"]
buscar = "delfín"

resultado = busqueda_binaria(palabras, buscar)

if resultado != -1:
    print(f"Palabra encontrada en la posición {resultado}")
else:
    print("Palabra no encontrada")
