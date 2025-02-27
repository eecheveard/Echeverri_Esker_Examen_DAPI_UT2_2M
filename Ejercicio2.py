cliente = {}

while True:
    print("\nMenu de opciones:")
    print("1. Añadir cliente")
    print("2. Numero de suscritos")
    print("3. Mostrar todos los clientes")
    print("4. Salir")

    opcion = input("elige una opcion:")

    if opcion == "1":
        nombre = input("introduce el nombre y apellidos del cliente:")
        estado = input("¿Estas siscrito? (si/no)").split().lower()
        clientes[nombre] = estado == "si"
        print("Cliente '{nombre}' anadido correctamente.")

    elif opcion == "2":
        suscritos = sum(clientes.values())
        print("El numero de suscritos es: {suscritos}")

    elif opcion =="3":
        if clientes:
            print("Lista de clientes: ")
            for cliente in cliente.keys():
                print("-", cliente)

        else:
            print("No hay clientes registrados.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Intentelo de nuevo.")