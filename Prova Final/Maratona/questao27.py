def special_list(lst):
    if len(lst) == 1:
        return lst
    
    prev = special_list(lst[1:])
    
    if lst[0] % 2 == 0:
        return prev + [lst[0]]

    return [lst[0]] + prev

lst = [2,4,5,7,10,13,18]

print(special_list(lst))