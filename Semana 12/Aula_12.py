def count_to_num(n):
    if n == 0:
        return
    for i in count_to_num(n-1):
        yield i
    yield n

gen = count_to_num(5)
print(gen)