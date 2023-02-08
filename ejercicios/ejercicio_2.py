if __name__ == "__main__":
    radius = float(input("Digite el radio de la esfera: "))


    def area_circulo(r):
        area = (3.1416) * r ** 2
        return area


    print(f"\nEl area del circulo de radio {radius} es {area_circulo(radius)}")