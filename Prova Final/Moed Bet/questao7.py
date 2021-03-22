def all_zero(lst):
    str_list = []
    for i in lst:
        str_list.append(str(i))

    counter = str_list.count("0")
    for i in range(counter):
        str_list.remove("0")
        str_list.append("0")

    for i in range(len(str_list)):
        if str_list[i] == "True":
            str_list[i] = True
        elif str_list[i] == "False":
            str_list[i] = False
        else:
            str_list[i] = int(str_list[i])
    return str_list




lst = [3, 1, True, 0, 2, 77, -12, 3, False, -5, 0, 1]

print(all_zero(lst))
