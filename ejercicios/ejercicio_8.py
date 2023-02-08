if __name__=="__main__":
    lista_ejemplo=[9,8,7,6,5,4,3,2,1]
    def invert_list (l):
        x=(len(l)-1)
        new_l=[]
        for i in range (len(l)):
            inv=l[x]
            new_l.append(inv)
            x=x-1
        return new_l

    print(f"\nLa lista dada, de manera invertida es {invert_list(lista_ejemplo)}")
