def foo1(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + foo1(lst[:-1])


print(foo1([1,2,3,4,5]))