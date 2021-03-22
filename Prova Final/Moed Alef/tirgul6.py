def func1(dct):
    for value in dct.values():
        print(value)
    
dct = {"a" : 1, "b" : 2, "c" : 3, "a" : 2}

def func2(dct):
    for key in dct.keys():
        print(key)

def func6(st, dct):
    set_dct = {key for key in dct.keys()}
    return set_dct.intersection(st)


def func7(st1, st2):
    dct = dict()
    for element1, element2 in zip(st1, st2):
        dct[element1] = element2
    return dct


st1 = {"a", "b", "c"}
st2 = {1,2,3}

# print(func7(st1, st2))

def func8(dct1, dct2):
    set1 = {key for key in dct1.keys()}
    set2 = {key for key in dct2.keys()}

    final_dct = dict()
    final_dct_keys = set1.union(set2)
    pass

def func9(dct):
    pass