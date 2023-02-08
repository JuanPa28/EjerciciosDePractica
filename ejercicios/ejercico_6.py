if __name__=="__main__":
    lista_ejemplo=[1,2,3,4,5,6,7,8,9,10]
    resultado=0
    for i in range (len(lista_ejemplo)):
        resultado=resultado + lista_ejemplo[i]

    print(f"\nEl resultado de la suma de los numeros de la lista dada es {resultado}")