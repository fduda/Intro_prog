def foo(lst1,lst2):
    counter = 0
    for element1,index1 in enumerate(lst1):
        for element2,index2 in enumerate(lst2):
            if element1 == element2 and index1 == index2:
                counter += 1

    return counter

def foo2(lst1,lst2):
    if foo(lst1,lst2) == len(lst1):
        return True
    return False


def func7(lst, letter):
    counter = 0
    for i in lst:
        for j in i:
            if j == letter:
                counter += 1
    return counter



def func8(lst1, lst2):
    dct_freq = dict()
    for i in lst1:
        dct_freq[i] = lst2.count(i)
    return list(dct_freq.values())

