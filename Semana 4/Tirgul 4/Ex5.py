def add_algarisms_1(n):
    string_number = str(n)
    addition = 0
    for i in string_number:
        number = int(i)
        addition += number
    return addition

def add_algarisms_2(n):
    string_number = str(n)
    addition = 0
    number_lst = []
    for i in string_number:
        number = int(i)
        number_lst.append(number)
    for i in number_lst:
        addition += i
    return addition