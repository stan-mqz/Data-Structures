# pila = []

# pila.append("A")
# pila.append("B")
# pila.append("C")

# print(pila)
# pila.append("D")
# pila.append('E')

def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    return pila.pop()


pila = []
push(pila, "A")
push(pila, "B")
push(pila, "C")

print("Elementos de la pila: ", pila)

elemento = pop.pila()