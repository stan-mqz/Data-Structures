# ==========================================
# Sistema de Turnos - Banco Los Manguitos
# Estructura de datos: Queue (Cola) FIFO
# ==========================================

# Lista vacía que usaremos como Queue
cola = []

# Contador para generar los tickets
numero_turno = 1


def registrar_cliente(nombre):
    """ENQUEUE: inserta al final (REAR) de la cola."""
    global numero_turno

    # Generamos ticket (ej: "T001")
    turno = f"T{numero_turno:03d}"
    cliente = [turno, nombre]

    # Insertamos al final de la lista
    cola.append(cliente)

    # Preparamos el siguiente número
    numero_turno += 1

    print("\nCliente registrado correctamente.")
    print("Turno asignado:", turno)
    print("Cliente:", nombre)


def ver_siguiente():
    """PEEK: consulta el FRONT sin retirarlo."""
    if cola:
        siguiente = cola[0]
        print("Próximo:", siguiente[1])
    else:
        print("Cola vacía")


def atender_cliente():
    """DEQUEUE: retira al cliente del FRONT."""
    if cola:
        cliente = cola.pop(0)
        print("Turno llamado:", cliente[0])
        print("Cliente:", cliente[1])
    else:
        print("No hay clientes para atender.")


def mostrar_cola():
    """Recorre la cola y muestra su tamaño (SIZE)."""
    if not cola:
        print("Vacío")
    else:
        for cliente in cola:
            print(cliente[0], "-", cliente[1])

        print("Total en espera:", len(cola))


# ------------------------------------------
# Menú principal
# ------------------------------------------
while True:
    print("\n================================")
    print("      BANCO LOS MANGUITOS")
    print("       SISTEMA DE TURNOS")
    print("================================")
    print("1. Registrar cliente")
    print("2. Ver próximo cliente")
    print("3. Llamar siguiente turno")
    print("4. Mostrar cola")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        registrar_cliente(nombre)
    elif opcion == "2":
        ver_siguiente()
    elif opcion == "3":
        atender_cliente()
    elif opcion == "4":
        mostrar_cola()
    elif opcion == "5":
        print("\nSistema finalizado.")
        break
    else:
        print("\nOpción no válida.")