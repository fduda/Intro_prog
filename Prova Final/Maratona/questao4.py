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
    for i in lst:
        if lst.count(i) % 2 == 1:
            return i

print(foo2([2,2,1,3,1,3,3,3,2]))