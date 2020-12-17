import random as rd
import copy
def factorial_rec(n):
    if n == 0:
        return 1
    return n*factorial_rec(n-1)


def my_pow(x,n):
    if n == 0:
        return 1
    return x*my_pow(x,n-1)

def my_pow2(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return my_pow2(x,n//2)*my_pow2(x,n//2)

# print(my_pow2(3,4))

def my_pow3(x,n):
    if n == 0:
        return 1
    # if n == 1:
    #     return x
    if n%2 == 1:
        return x*my_pow3(x,n-1)
    t = my_pow3(x,n//2)
    return t*t

def merge(a,b): # a and b 
    size_1 = len(a) 
    size_2 = len(b) 
    
    res = [] 
    i, j = 0, 0
  
    while i < size_1 and j < size_2: 
        if a[i] < b[j]: 
            res.append(a[i]) 
            i += 1
    
        else: 
            res.append(b[j]) 
            j += 1
    
    res = res + a[i:] + b[j:] 
    return res

a = []
# b = []
while len(a) < 16:
    a.append(rd.randrange(10))
    a.sort()

# while len(b) < 10:
#     b.append(rd.randrange(10))
#     b.sort()

# a = [5,7,8]
# b = [1,4,9]

def merge_sort(arr): #len(a) is a power of 2
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2

    l_arr = arr[:mid]
    r_arr = arr[mid:]
    l_arr = merge_sort(l_arr)
    r_arr = merge_sort(r_arr)

    return merge(l_arr,r_arr)


def reverse(n): # n is the number of lines to receive
    if n == 0:
        return 
    inp = input("enter text: ")

    reverse(n-1)
    print(inp)

reverse(3)
