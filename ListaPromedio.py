#Lista Vacia
ListaPromedio = [2.2,1.2,3.3,4.5,5,2,3,4.3,2.1,5]

print(f"Lista{ListaPromedio}")

suma_total = 0
cantidad_elementos = 0

#Promedio
for numero in ListaPromedio:
    suma_total += numero
    cantidad_elementos += 1

promedio = float(suma_total/cantidad_elementos)

print(f"Promedio: {promedio:.2f}")

print("Resultados de la comparación:")
for numero in ListaPromedio:
    if numero > promedio:
        print(f"El número {numero} es Mayor que el promedio.")
    elif numero < promedio:
        print(f"El número {numero} es Menor que el promedio.")
    else:
        print(f"El número {numero} es Igual al promedio.")
