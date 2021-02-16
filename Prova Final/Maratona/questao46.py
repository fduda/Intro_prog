arr46 = iter([3,1,2,4,1])

def q46(original_iter):
    for i in original_iter:
        for j in range(i):
            yield i


a = q46(arr46)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

