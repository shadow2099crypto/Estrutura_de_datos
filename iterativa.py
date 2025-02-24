def factorial_iterativo(n):
    if n < 0:
        return "⚠️ No se puede calcular el factorial de un número negativo."
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i  
        
    return resultado

def interactivo():
    while True:
        entrada = input("\nIngrese un número entero (o 'q' para salir): ").strip()
        
        if entrada.lower() == 'q': 
            print("Saliendo del programa...")
            break
        
        try:
            num = int(entrada)
            if num > 100000:  
                print("⚠️ El cálculo de factoriales de números muy grandes puede tomar tiempo.")
            print(f"El factorial de {num} es: {factorial_iterativo(num)}")
        except ValueError:
            print("⚠️ Error: Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    print("Cálculo del Factorial en Modo Iterativo\n")
    interactivo()

