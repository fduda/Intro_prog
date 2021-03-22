def most_common(lst):

    dict_names_freq = dict()

    for name in lst:
        if name not in dict_names_freq:
            dict_names_freq[name] = 1
        else:
            dict_names_freq[name] += 1

    list_freq = dict_names_freq.values()
    greates_freq = max(list_freq)
    final_list = []

    for key, value in dict_names_freq.items():
        if value == greates_freq:
            final_list.append(key)
    
    return final_list


def most_common2(lst):
    dct = {}
    for i in lst:
        dct[i] = dct.get(i,0) + 1
    return max(dct, key=dct.get)


lst = ["bob","alice" ,"alice","carol","carol","carol","alice"]

print(most_common(lst))