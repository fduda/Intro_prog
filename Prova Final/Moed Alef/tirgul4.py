from typing import List


def func1(lst):
    maximum = lst[0]

    for i in range(len(lst)):
        if lst[i]>maximum:
            maximum = lst[i]
    return maximum



def func2(lst):
    maximum = func1(lst)
    for index, element in enumerate(lst):
        if element == maximum:
            return index

# print(func2(lst = [1,4,2,5,63,1,2,56,1,213,215,62]))

def func3(lst):
    maximum = 0

    for i in lst:
        if type(i) == list:
            for j in i:
                if j>maximum:
                    maximum = j
    return maximum

def func5(n):
    number_str = str(n)
    total = 0
    for algarism in number_str:
        total += int(algarism)
    return total

def func5b(n):
    number_str = str(n)
    if len(number_str) == 1:
        return number_str[-1]
    
def func6(lst, x):
    low = 0
    high = len(lst)-1
    mid = 0

    while low <= high:
        mid = (low+high)//2
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid -1
        else:
            return True
    return False


lst = [[1,2,3], 4, [5, 6], 1]
s = 0
for i in range(len(lst)):
    if type(lst[i]) == list:
        for j in range(len(lst[i])):
            s += lst[i][j]
    else:
        s += lst[i]
print(s)


def f(lst):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            lst[i] = 0
    print(sum(lst))
f(lst)
print(sum(lst))