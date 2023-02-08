if __name__=="__main__":
    lista_ejemplo=[7,1,8,2,9,3,6,4,5]
    n_mayor=0
    n_menor=lista_ejemplo[0]

    for i in range (len(lista_ejemplo)):
        if lista_ejemplo[i] > n_mayor:
            n_mayor=lista_ejemplo[i]
        if lista_ejemplo[i]<n_menor:
            n_menor=lista_ejemplo[i]

    print(f"\nEl numero mas grande de la lista dada es el {n_mayor} y el numero mas pequeño de la lista dada es el {n_menor}")