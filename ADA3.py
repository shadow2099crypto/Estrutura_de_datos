def intercalacion(lista1, lista2):
    resultado = []
    i = j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:] + lista2[j:]
    return resultado
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print("Intercalación:", intercalacion(a, b))


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return intercalacion(izquierda, derecha)
lista = [7, 2, 9, 4, 1]
print("Mezcla Directa:", merge_sort(lista))


def mezclaequilibrada(lista):
    mid = len(lista) // 2
    archivo1 = sorted(lista[:mid])
    archivo2 = sorted(lista[mid:])
    return intercalacion(archivo1, archivo2)
datos = [20, 0, 5, 200, 125, 25]
print("Mezcla Equilibrada:", mezclaequilibrada(datos))