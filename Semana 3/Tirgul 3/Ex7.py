def lista_letra(lista_string, letra):
    counter = 0
    for i in lista_string:
        for j in i:
            if j == letra:
                counter += 1
    return counter

print(lista_letra(["abc", "aaa", "csa", "c"], "c"))