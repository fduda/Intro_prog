def positive_elements_in_list(lista):
    """
    docstring
    """
    counter = 0

    for i in lista:
        if i > 0:
            counter += 1

    return counter


print(positive_elements_in_list([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]))
