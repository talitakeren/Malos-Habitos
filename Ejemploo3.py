# Función para calcular el área de un rectángulo
def Calcular_AreaRectangulo(LadoLargo, LadoAncho):
    AreaRectangulo = LadoLargo * LadoAncho
    return AreaRectangulo

# Función para calcular el área de un triángulo
def Calcular_AreaTriangulo(Base, Altura):
    AreaTriangulo = 0.5 * Base * Altura
    return AreaTriangulo

# Función principal
def main():

    print("------ÁREA DE UN RECTÁNGULO-------")
    Largo = float(input("Ingrese el ancho del rectangulo: "))
    Ancho = float(input("Ingrese el largo del rectangulo: "))
    rect_area = Calcular_AreaRectangulo(Largo, Ancho)
    print("El área del rectángulo es:")
    print(f"{Largo} * {Ancho} = {rect_area}")
    print("----------------------------------\n")

    print("------ÁREA DE UN TRIÁNGULO-------")
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    tri_area = Calcular_AreaTriangulo(base, altura)
    print("El área del triángulo es:")
    print(f"0.5 * {base} * {altura} = {tri_area}")
    print("----------------------------------")

main()
