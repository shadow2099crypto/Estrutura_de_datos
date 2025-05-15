precios = {
    "manzana": 10,
    "banana": 6,
    "sandía": 25,
    "naranja": 8,
    "pera": 12,
    "figura de acción": 300,
    "audífonos": 250,
    "computador": 7500,
    "tablet": 3400
}

print("📦 Consulta de precios de productos. Escribe 'salir' para terminar.\n")

while True:
    producto = input("🛒 Escribe el nombre del producto: ").lower()
    
    if producto == "salir":
        print("👋 Gracias por usar el sistema de consulta. ¡Hasta luego!")
        break

    if producto in precios:
        print(f"✅ El precio de '{producto}' es ${precios[producto]}\n")
    else:
        print("❌ Producto no encontrado. Intenta con otro nombre.\n")
