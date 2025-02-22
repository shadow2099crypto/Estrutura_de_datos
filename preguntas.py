def quiz():
    preguntas = [
        {
            "pregunta": "¿Qué estructura se usa para repetir un bloque de código un número determinado de veces?",
            "opciones": ["a) if", "b) for", "c) while", "d) try"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Cuál de las siguientes opciones NO es un tipo de dato en Python?",
            "opciones": ["a) int", "b) str", "c) bool", "d) loop"],
            "respuesta": "d"
        },
        {
            "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
            "opciones": ["a) define", "b) func", "c) def", "d) function"],
            "respuesta": "c"
        }
    ]
    
    puntaje = 0
    
    for i, p in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {p['pregunta']}")
        for opcion in p["opciones"]:
            print(opcion)
        respuesta_usuario = input("\nTu respuesta: ").strip().lower()
        
        if respuesta_usuario == p["respuesta"]:
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era '{p['respuesta']}'.")
    
    print(f"\nTu puntaje final es: {puntaje}/{len(preguntas)}")

if __name__ == "__main__":
    print("📝 ¡Bienvenido al Quiz de Python!\n")
    quiz()
