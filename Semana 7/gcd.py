import time
import math


def gcd (x, y):
    for i in range(1, min(x,y) + 1):
        if x%i == 0 and y%i == 0:
            divisor = i
    return divisor




# start = time.time()

# print(gcd(272835546 ,870453489))
# print("Time taken: ", round(time.time() - start,2), " seconds")

# start = time.time()
# print(gcd_euclide(272835546,870453489))
# print("Time taken: ", round(time.time() - start, 2)," seconds") 


# def f(n):
#     sum = 0
#     for i in range(n):
#         for j in range(i):
#             sum += (i+j)
#     return sum


# print(f(3))

def f(x,y):
    r = 1
    for i in range(y):
        r = r*x
    return r





def gcd_euclide(x, y):
    counter = 0
    while y>0:
        x,y = y, x%y
        counter +=1
    print(counter)
    return x


print(gcd_euclide(1000000, 3000000))