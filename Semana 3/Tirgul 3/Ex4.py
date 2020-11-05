def same_elements(lista1, lista2):
    counter = 0

    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            counter += 1
    return counter
                
print(same_elements([1,3,2,4,7],[1,6,3,4,7]))