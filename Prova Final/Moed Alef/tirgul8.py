def func1(n):
    if n ==0:
        return 0
    return (n%10 + func1(n//10))

def func2(lst):
    if len(lst) == 0:
        return 0
    return lst[-1] + func2(lst[:-1])

# print(func2([1,2,3]))

def func3(string):
    if len(string) == 0:
        return ""
    return string[-1] + func3(string[:-1])


def func5(lst, num):
    if lst[0] == num:
        return True
    elif len(lst) == 1:
        return False
    return func5(lst[1:], num)


def func6(lst, num):
    low = 0
    high = len(lst) -1
    mid = 0

    while high > low:
        mid = (high + low)//2

        if lst[mid] < num:
            low = mid+1
        elif num < lst[mid]:
            high = mid-1
        else:
            return True
    return False

def func4(lst1, lst2):
    counter = 0

    if len(lst1) == 0:
        return counter
    elif lst1[0] == lst2[0]:
        counter += 1
        return func4(lst1[1:], lst2[1:])
    return counter


lst1 = [1,2,3]
lst2 = [1,5,3]

print(func4(lst1, lst2))
# print(lst1[1:])
