from typing import final


def filter_common(lst):
    dct = {}
    for i in lst:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    
    final_list = []
    for key, value in dct.items():
        if dct[key] >= 2:
            final_list.append(key)
    return final_list

def filter_common2(lst):
    return list({i for i in lst if lst.count(i) > 1})

lst = ["Guiness", "Corona", "Heineken", "Budweiser", "Corona", "Guiness", "Amstel", "Corona"]

print(filter_common(lst))