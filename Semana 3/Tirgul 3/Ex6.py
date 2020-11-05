def list_and_number(lista, number):
    for i in lista:
        if lista[i] == number:
            return True
        else:
            return False

print(list_and_number([1,2,3,4],6))