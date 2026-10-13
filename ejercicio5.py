
import random

def ejercicio5():
    entero = random.randint(1,20)
    print("adivina el numero secreto")


    for i in range(5):
        print(f"intento numero: {i+1}")
        
        numero = int(input("ingrese el numero: "))
        if numero == entero:
            print("el numero es el correcto")
            break
        elif numero > entero:
            print("el numero es menor al indicado")
        elif numero < entero:
            print("el numero es mayor al indicado")
    else:
        print(f"te haz quedado sin intentos; el numero era {entero}")


