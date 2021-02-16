# def count_to_num(n):
#     if n == 0:
#         return 
#     yield from count_to_num(n-1)
#     yield n

# for i in count_to_num(0):
#     print(i)


import math
def compose(g):
    def comp(f):
        return lambda x: g(f(x))
    return comp

h = compose(math.cos)
g = h(math.sqrt)