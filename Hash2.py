estudiantes = {
    "2023001": "Ingeniería en Sistemas",
    "2023002": "Arquitectura",
    "2023003": "Administración",
    "2023004": "Derecho",
    "2023005": "Medicina",
    "2023006": "Psicología",
    "2023007": "Diseño Gráfico",
    "2023008": "Contaduría Pública",
    "2023009": "Ingeniería Civil",
    "2023010": "Ingeniería Mecánica",
    "2023011": "Marketing Digital",
    "2023012": "Biología",
    "2023013": "Ingeniería Industrial"
}

print(" Consulta de carreras por matrícula. Escribe 'salir' para terminar.\n")

while True:
    matricula = input("🔎 Escribe la matrícula del estudiante: ")

    if matricula.lower() == "salir":
        print(" Consulta finalizada. ¡Hasta luego!")
        break

    if matricula in estudiantes:
        print(f"✅ Estudiante inscrito en: {estudiantes[matricula]}\n")
    else:
        print("❌ Matrícula no registrada. Intenta con otra.\n")
