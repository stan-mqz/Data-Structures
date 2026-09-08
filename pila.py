pila=[]

pila.append("Iniciar sesion")

pila.append("Consultar el perfil")
pila.append("Ver amigos en comun")
pila.append("Ola k ase")




print('Pila actual:')
print(pila)


accion = pila.pop("\n Accion reitrada:")
print(accion)

accion = pila.pop("\n Penultima accion reitrada:")
print(pila)

