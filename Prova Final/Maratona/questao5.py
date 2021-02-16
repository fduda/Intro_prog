def foo(lst):
    freq_dict = dict()
    for number in lst:
        if number not in freq_dict:
            freq_dict[number] = 1
        else:
            freq_dict[number] += 1
    
    for key,value in freq_dict.items():
        if value%2 == 1:
            return key



def foo2(lst):
    return lst.index(foo(lst))
