def magic_number(n):
    number_str = str(n)
    square_list = []
    for i in number_str:
        i = int(i)
        square_list.append(str(i**2))
    return int("".join(square_list))


print(magic_number(1769))
