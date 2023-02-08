if __name__=="__main__":
    numero=int(input("Digite el numero a calcularle el factorial: "))
    def factorial_numero(n):
        if n>0:
            resultado=1
            for i in range (1, n+1):
                resultado=resultado*i
        elif n==0:
            resultado=1
        else:
            return ("\n¡ERROR! El numero no puede ser negativo")
        return resultado

    print(f"\nEl factoorial del numero {numero} es {factorial_numero(numero)}")