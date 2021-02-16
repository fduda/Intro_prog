arr47 = iter([2,2,8,8,1,0,0,4,5])

def runnin_average_iterator(iterator):
    lst = []
    for i in iterator:
        lst.append(i)
        yield sum(lst)/len(lst)

a = runnin_average_iterator(arr47)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
