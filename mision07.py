#Sara Delgado
#misión

# dividir
def dividir(residuo, divisor):
    cociente = 0

    while residuo >= divisor:
        residuo = residuo - divisor

        cociente = cociente + 1

    print("El residuo es: ", residuo)

    print("El cociente es: ", cociente)


# encontrar mayor

def encontrarMayor():
    print("Teclea una serie de numeros para encontrar el mayor")
    num = int(input("Escribe un número positivo [ -1 para salir]: "))

    mayor = num

    while num != -1:

        num = int(input("Escribe un número positivo [ -1 para salir]: "))

        if num > mayor:
            mayor = num

        if mayor == -1:
            print("No hay valor mayor")

        else:

            print("El mayor es ", mayor)


def main():
    salir = False

    while not salir:

        print("""Sara Delgado 
        A01745952
        Menu
        1. Calcular divisiones
        2. Encontrar mayor
        3. Salir
        """)
        menu = int(input("Teclea tu opción"))

        if menu == 1:

            residuo = int(input("Escribe el dividendo: "))
            divisor = int(input("Escribe el divisor: "))
            dividir(residuo, divisor)
        elif menu == 2:
            encontrarMayor()

        elif menu == 3:
            print("Regresa pronto")
            salir = True

        elif menu:
            print ("Teclea una opción del 1 - 3")


main()
