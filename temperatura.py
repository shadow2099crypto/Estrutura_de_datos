def main():
 
    cantidad_dias = int(input("Ingrese la cantidad de días: "))
    
    temperaturas = []
    
    for i in range(cantidad_dias):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)

    promedio = sum(temperaturas) / len(temperaturas)
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    dias_superiores = sum(1 for temp in temperaturas if temp > promedio)
    
    print(f"\nTemperatura promedio: {promedio:.2f}°C")
    print(f"Temperatura más alta: {temp_max}°C")
    print(f"Temperatura más baja: {temp_min}°C")
    print(f"Días con temperatura superior al promedio: {dias_superiores}")

if __name__ == "__main__":
    main()