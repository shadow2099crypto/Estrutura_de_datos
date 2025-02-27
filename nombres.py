def obtener_nombres(cantidad):
    nombres = []
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres.append(nombre)
    return nombres

def calcular_longitudes(nombres):
    return [len(nombre) for nombre in nombres]

def mostrar_resultados(nombres, longitudes):
    print("\nResultados:")
    for nombre, longitud in zip(nombres, longitudes):
        print(f"{nombre}: {longitud} caracteres")

def main():
    cantidad = int(input("Ingrese la cantidad de nombres: "))
    a = obtener_nombres(cantidad)
    longitudes = calcular_longitudes(a)
    mostrar_resultados(a , longitudes)

if __name__ == "__main__":
    main()
