if __name__=="__main__":
    import random
    filas=int(input("Digite el numero de filas que tendra la matriz: "))
    columnas=int(input("Digite el numero de columnas que tendra la matriz: "))
    def generador_matriz(f, c):
        matriz = [[random.randint(0, 100) for i in range(c)] for i in range(f)]
        return matriz
    def print_matriz(matriz):
        for i in matriz:
            print(i)

    matriz= generador_matriz(filas, columnas)

    print_matriz(matriz)