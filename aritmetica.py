import re

class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

def tokenize(expresion):

    tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/]', expresion)
    return tokens

def evaluar_posfija(expresion):
    pila = Pila()
    tokens = tokenize(expresion)
    for token in tokens:
        try:
            num = float(token)
            pila.push(num)
        except ValueError:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                resultado = a / b
            else:
                print("Operador no reconocido:", token)
                return None
            pila.push(resultado)
    return pila.pop()

def evaluar_prefija(expresion):
    pila = Pila()
    tokens = tokenize(expresion)
    for token in reversed(tokens):
        try:
            num = float(token)
            pila.push(num)
        except ValueError:
            a = pila.pop()
            b = pila.pop()
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                resultado = a / b
            else:
                print("Operador no reconocido:", token)
                return None
            pila.push(resultado)
    return pila.pop()

def main():
    while True:
        modo = input("Elige el modo de evaluación (prefijo/posfijo) o 's' para salir: ").strip().lower()
        if modo == 's':
            print("Saliendo del programa...")
            break
        if modo == "posfijo":
            print("Ejemplo para notación posfijo: 3 4+5*   (equivale a (3+4)*5)")
            expresion = input("Ingresa la expresión en notación posfijo: ")
            resultado = evaluar_posfija(expresion)
        elif modo == "prefijo":
            print("Ejemplo para notación prefijo: + 3 4")
            expresion = input("Ingresa la expresión en notación prefijo: ")
            resultado = evaluar_prefija(expresion)
        else:
            print("Modo no reconocido. Por favor, elige 'prefija', 'posfija' o 's' para salir.")
            continue
        print("El resultado es:", resultado)
        print()  

if __name__ == "__main__":
    main()
