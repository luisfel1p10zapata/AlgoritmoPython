def ejercicio3():
    print("Ejercicio 25. Buscar nombres")

    # lista de aprendices
    nombres = ["sebastian", "Juliana", "Adrian", "rubigol", "messi", "Ana", "carvajal", "Maria paz", "Jorge", "Luis"]
    
    # pedir el nombre
    nombre = input("ingrese el nombre que desea buscar: ")
    
    #verificamos si existe
    if nombre in nombres:
        posicion = nombres.index(nombre)
        print("el nombre si existe en la lista")
        print("posicion:", posicion + 1)
    else:
        print("el nombre no existe en la lista")