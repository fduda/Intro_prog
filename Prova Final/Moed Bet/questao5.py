def foo(lst):
    for i in lst:
        if lst.count(i) % 2 != 0:
            return i

print(foo([1,1,2,2,3,3,4,4,5,5,6,8,8,9,9,1,1]))

def foo2(lst):
    element = foo(lst)
    for i in range(len(lst)):
        if lst[i] == element:
            return i

print(foo2([1,1,2,2,3,3,4,4,5,5,6,8,8,9,9,1,1]))