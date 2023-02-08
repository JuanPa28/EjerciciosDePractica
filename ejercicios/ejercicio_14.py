if __name__=="__main__":
    lista_ejemplo=[1,2,3,4,5,6,7,8,9]

    sum_elementos=0
    for i in range (len(lista_ejemplo)):
        sum_elementos=sum_elementos+lista_ejemplo[i]

    resultado=sum_elementos/len(lista_ejemplo)

    print(f"La media aritmetica de la lista dada {lista_ejemplo} es = {resultado}")