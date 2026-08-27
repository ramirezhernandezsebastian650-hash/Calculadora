def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            a = 1
        elif opcion == '2':
            a = 2
        elif opcion == '3':
            a = 3
        elif opcion == '4':
            a = 3
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")