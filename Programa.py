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
            num1 = float(input("Ingrese el un número: "))
            num2 = float(input("Ingrese el otro número: ")) 
            resultado = num1 + num2
            print(f"el resultado de la suma es:{resultado}")
        elif opcion == '2':
            a = 2
            num1 = float(input("Ingrese el un número: "))
            num2 = float(input("Ingrese el otro número: ")) 
            resultado = num1 + num2
            print(f"el resultado de la suma es:{resultado}")
        elif opcion == '3':
            num1 = float(input("Ingrese el un número: "))
            num2 = float(input("Ingrese el otro número: "))
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")