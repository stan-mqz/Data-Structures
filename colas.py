# cola = []

# cola.append("Ana")
# cola.append("Carlos")
# cola.append("Luis")

# print(f"Cola: {cola}")

colaTienda = []

colaTienda.append("Ana")
colaTienda.append("Carlos")
colaTienda.append("Luis")


print("Cliente de la Tienda Rosita:", colaTienda[0])

print("Clientes en espera", len(colaTienda))


cliente  = colaTienda.pop(0)

print("Los clientes de la cola son:", colaTienda)

print("El ultimo cliente:", colaTienda[-1] )

if not colaTienda:
    print("No hay clientes esperando")
else:
    print("Todavia hay clientes esperando")