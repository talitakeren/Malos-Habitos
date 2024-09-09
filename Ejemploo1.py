def multiplicacion(factor1, factor2):
    Producto = factor1 * factor2
    return Producto

if __name__=="__main__":
    multiplicando = float(input("Ingrese Multiplicando: "))
    multiplicador = float(input("Ingrese Multiplicador: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")