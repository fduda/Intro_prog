def foo3(lst):
    if len(lst) == 0:
        return 0

    return lst[-1] + foo3(lst[:-1])

print(foo3([1,2,3,4,5]))