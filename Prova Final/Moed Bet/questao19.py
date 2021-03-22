def filter_common(lst):
    dct = {}
    for i in lst:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    final_list = [key for key, value in dct.items() if value >1]
    return final_list

beer = ["Guinness", "Corona", "Heineken", "Budweiser", "Corona", "Guinness", "Amstel", "Corona"]
print(filter_common(beer))