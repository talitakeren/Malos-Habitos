def multiplicacion(factor1, factor2):
    sumando1 = factor1 * factor2
    return sumando1

def suma(sumando2):
    return sumando2

if  __name__=="__main__":
    print("\n----- RESOLVIENDO OPERACIÓN MATEMÁTICA ------\n")
    numero1 = float(input("Ingrese primer número: "))
    numero2 = float(input("Ingrese segundo número: "))
    numero3 = float(input("Ingrese tercer número: "))

    resultado = multiplicacion(numero1, numero2) + suma(numero3)
    print("El resultado es: "f"{numero1} * {numero2} + {numero3} = {resultado}")