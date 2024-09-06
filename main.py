import sumar
import restar
import multiplicar
import dividir
import suma_avanzada

def menu():
    print("Elige una opcion:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Suma avanzada")
    print("6- Salir")

while True:
    menu()
    opcion = input("Ingresa una opción: ")

    if opcion == "1":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        print("El resultado de la suma es:", sumar.sumar(a, b))

    elif opcion == "2":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        print("El resultado de la resta es:", restar.restar(a, b))

    elif opcion == "3":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        print("El resultado de la multiplicacion es:", multiplicar.multiplicar(a, b))

    elif opcion == "4":
        a = float(input("Ingresa el numero dividendo: "))
        b = float(input("Ingresa el numero divisor: "))
        print("El resultado de la division es:", dividir.dividir(a, b))

    elif opcion == "5":
        numeros = input("Ingresa los numeros a sumar agregando un espacio entre cada uno: ").split()
        numeros = [float(num) for num in numeros]
        print("El resultado de la suma avanzada es:", suma_avanzada.suma_avanzada(numeros))

    elif opcion == "6":
        print("Fin de los calculos")
        break

    else:
        print("La opcion seleccionada no existe, ingresa una opcion valida.")
