def mcd(a, b):
    """Calcula el Máximo Común Divisor (MCD) usando recursión."""
    if b == 0:
        return a
    return mcd(b, a % b)

def interactivo():
    """Ejecuta el programa de manera interactiva."""
    try:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = mcd(num1, num2)
        print(f"El Máximo Común Divisor de {num1} y {num2} es: {resultado}")
    except ValueError:
        print("⚠️ Error: Por favor, ingresa números enteros válidos.")
        interactivo()  

if __name__ == "__main__":
    print(" Cálculo del Máximo Común Divisor (MCD) usando Recursión \n")
    interactivo()
