def ejercicio4():
    numeros = []

    for i in range(10):
        numero = float(input(f"ingrese el numero {i+1}: "))
        numeros.append(numero)

    mayor = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

    print(f"este es el numero mayor: {mayor}")
    print(f"este es el numero menor: {menor}")