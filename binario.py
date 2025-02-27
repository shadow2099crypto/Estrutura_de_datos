def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número entero positivo: "))

if num < 0:
    print("Por favor, ingrese un número entero positivo.")
elif num == 0:
    print("El equivalente en binario es: 0")
else:
    print("El equivalente en binario es:", decimal_a_binario(num))