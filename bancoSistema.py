# Sistema de un banco
# Banco los manguitos

cola = [] # creamos una cola vacia que sera usada globalmente
numero_turno = 1 # Variable global para contabilizar los clientes

def registrar_clientes(nombre):
    global numero_turno # Declaramos la variable global para poder modificarla

    # Generar el codigo de turno
    # T = letra que significa turno, :03d minimo de digitos para rellenar son 3 
    # Ejemplo: T001
    
    turno = f"T{numero_turno:03d}" # Generamos el turno con formato T001, T002, etc.
    cliente = [turno, nombre] # Creamos una lista con el turno y el nombre del cliente
    cola.append(cliente) # Agregamos el cliente a la cola
    numero_turno += 1 # Incrementamos el numero de turno para el siguiente cliente

    # Imprimamos el resultado
    print("\nCliente registrado correctamente.")
    print("Turno asignado: ", turno)
    print("Cliente: ", nombre)


    
def ver_siguiente(): # Esto permite ver el siguiente cliente en espera
    if cola:
        siguiente= cola[0]
        print("\nSiguiente cliente en espera:")
        print("Turno:", siguiente[0])
        print("Nombre:", siguiente[1])
    else:
        print("\nNo hay clientes en espera.") 

def atender_cliente(): 
    if cola: 
        cliente = cola.pop(0) # Eliminamos el primer cliente de la cola
        print("\nAtendiendo al cliente:")
        print("Turno:", cliente[0])
        print("Nombre:", cliente[1])
    else:
        print("\nNo hay clientes que atendeer. =).")


def mostrar_cola():

    if not cola:
        print("No hay clientes esperando")
    else:
        for cliente in cola:
            print(cliente[0], " - ")

    print("\n Cantidad de clientes que esperan ", len(cola))

    print("Ultimo turno ", cola[-1][0])


while True:

    print("\n")        
    print("Banco Los Manguitos")        
    print("-- Menu de Turnos --")        
    print("-- 1 Registrar clientes --")        
    print("-- 2 Ver proximos clientes --")        
    print("-- 3 Llamar al cliente --")        
    print("-- 4 Mostrar todos los clientes --")        
    print("-- 5 Salir --")

    opcion = input("Seleccione una opcion (Numero):")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")        
        registrar_clientes(nombre)

    elif opcion == '2':
        ver_siguiente()


    elif opcion == '3':
        atender_cliente()

    elif opcion == '4':
        mostrar_cola()
    elif opcion == "5":
        print("\n Sistema finalizado")
        break

    else:
        print("\n La opcion seleccionada no existe")