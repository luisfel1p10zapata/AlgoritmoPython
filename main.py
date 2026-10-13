from ejercicio1 import ejercicio1
from ejercicio2 import ejercicio2
from ejercicio3 import ejercicio3
from ejercicio4 import ejercicio4
from ejercicio5 import ejercicio5


def mostrar_menu():
    print("\n========== MENU DE EJERCICIOS ==========")
    print("1. Conteo de pares e impares")
    print("2. Ejercicio del integrante 2")
    print("3. Buscar nombres")
    print("4. Identificar numero mayor y menor")
    print("5. Adivina el numero secreto")
    print("0. Salir")
    print("========================================")


def main():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: ingrese un numero valido.")
            continue

        match opcion:
            case 1:
                ejercicio1()
            case 2:
                ejercicio2()
            case 3:
                ejercicio3()
            case 4:
                ejercicio4()
            case 5:
                ejercicio5()
            case 0:
                print("Gracias por utilizar el programa.")
                break
            case _:
                print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()