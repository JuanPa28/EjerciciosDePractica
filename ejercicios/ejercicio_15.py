if __name__=="__main__":
    cadena=input("Digite la palabra a evaluar: ")
    def palindromo(c):
        inicio = 0
        fin = len(c) - 1
        while c[inicio] == c[fin]:
            if inicio >= fin:
                return True
            inicio= inicio + 1
            fin= fin - 1
        return False

    if palindromo(cadena):
        print("\nLa palabra es Palidroma")
    else:
        print("\nLa palabra NO es Palidroma")
