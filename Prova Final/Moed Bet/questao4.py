def foo(lst):
    for i in lst:
        if lst.count(i) % 2 != 0:
            return i

print(foo([1,1,2,2,3,3,4,4,5,5,6,8,8,9,9,1,1]))