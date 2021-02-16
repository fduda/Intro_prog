from questao43 import P


arr49 = iter([1,3,5,8,2,1,10,10])


def diff_iter(iterator):
    prev = next(iterator)
    for i in iterator:
        yield i - prev
        prev = i


a = diff_iter(arr49)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
