def ejercicio1():
    pares=0
    impares=0
    suma_pares=0

    for numero in range(1, 101):
        if numero % 2 == 0:
            pares +=1
            suma_pares += numero
        else:
            impares +=1
    print(f"La cantidad de números pares es: {pares}")
    print(f"La cantidad de números impares es: {impares}")
    print(f"La suma de los números pares es: {suma_pares}")

    