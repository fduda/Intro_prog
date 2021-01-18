# def count_to_num(n):
#     if n == 0:
#         return 
#     yield from count_to_num(n-1)
#     yield n

# for i in count_to_num(0):
#     print(i)


x = ['-4', '-41', '15', '4', '5', '51']

z = sorted(x, key=lambda y: int(y) )
print(z)