import tkinter as tk
from tkinter import simpledialog


def memoria_estatica():
    calificaciones = [0] * 5
    root = tk.Tk()
    root.withdraw()  
    
    for i in range(5):
        calificaciones[i] = int(simpledialog.askstring("Entrada", f"Captura la calificación {i + 1}:"))
    
    print("Calificaciones ingresadas:")
    for i, cal in enumerate(calificaciones, start=1):
        print(f"Calificación {i}: {cal}")


def memoria_dinamica():
    frutas = ["Mango", "Manzana", "Banana", "Uvas"]
    print("Lista de frutas inicial:", frutas)
    
    frutas.pop(0)  
    frutas.pop(1)  
    
    frutas.append("Sandía")
    print("Lista de frutas:", frutas)

memoria_estatica()
memoria_dinamica()