def compress(lst):
    res = []
    s = 0
    for i in range(len(lst)):
        s += 1
        if i == len(lst) - 1 or lst[i] != lst[i+1]:
            res.append((lst[i], s))
            s = 0
    return res



def compress2(lst):
    number_of_appereances = [1]
    elements = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i-1] == lst[i]:
            number_of_appereances[-1] += 1
        else:
            number_of_appereances.append(1)
            elements.append(lst[i])
    packed_list = [[i]*j for i,j in zip(elements, number_of_appereances)]

    final_list = [(i[0],len(i)) for i in packed_list]
    return final_list


print(compress2(lst = ["a","a","b","b","b","c","a","a"]))
