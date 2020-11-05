def func(lista1, lista2):
    """
    docstring
    """
    lista_final = [] # list(range(len(lista1)))

    for i in lista1:
        counter = 0
        for j in lista2:
            if i == j:
                counter += 1
        
        lista_final.append(counter)
 

    return lista_final

print(func([1,3,2,4,5], [1,1,4,4,22,1,6,2,5,4]))