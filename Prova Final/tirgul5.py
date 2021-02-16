def func5(lst1, lst2):
    if len(lst1) == len(lst2):
        final_list = [lst1[i] + lst2[i] for i in range(len(lst1))]
    elif len(lst1) > len(lst2):
        final_list = [lst1[i] + lst2[i] for i in range(len(lst2))] + lst1[len(lst2):]
    elif len(lst1) < len(lst2):
        final_list = [lst1[i] + lst2[i] for i in range(len(lst1))] + lst2[len(lst1):]
    return final_list

def func6(lst):
    final_list = []
    for i in lst:
        final_list.append(i[::-1])
    return final_list

def func7(lst):
    final_list = []
    for i in lst[::-1]:
        final_list.append(i[::-1])
    return final_list
    
print(func7(["ab", "a","afs"]))
