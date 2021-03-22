from typing import final


def func1(lst):
    res = 0
    for i in lst:
        res += i
    return res

def func2(lst):
    res = 1
    for i in lst:
        res *= i
    return res

def func3(lst):
    highest = 0
    for i in lst:
        if i>highest:
            highest = i
    return highest

def func4(lst):
    lowest = 0
    for i in lst:
        if i < lowest:
            lowest = i
    return lowest


def func5(lst):
    counter = 0
    for i in lst:
        if len(i) > 2 and i[0] == i[-1]:
            counter += 1
    return counter


def last(lst): return lst[-1]
def func6(lst):
    return sorted(lst, key=last)

def func7(lst):
    final_set = set()
    for i in lst:
        final_set.add(i)
    return list(final_set)

def func8(lst):
    if len(lst) == 0:
        return True
    return False

def func11(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    intersection = set1.intersection(set2)
    if len(intersection) > 0:
        return True
    return False

def func12(lst):
    return [x for (i, x) in enumerate(lst) if i not in (0,4,5)]

def func14(lst):
    return [x for x in lst if x%2 == 1]





def merge(arr1, arr2):
    size_1 = len(arr1)
    size_2 = len(arr2)

    res = []
    i, j = 0, 0
    
    while i < size_1 and j < size_2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res = res + arr1[i:] + arr2[j:]
    return res

# arr1 = [1,5,6,9,11]
# arr2 = [3,4,7,8,10]

# print(merge(arr1,arr2))




def power_replicate(lst):
    number_of_apereances = [1]
    elements = [lst[0]]

    for i in range(1,len(lst)):
        if lst[i-1] == lst[i]:
            number_of_apereances[-1] += 1
        elif lst[i-1] != lst[i]:
            number_of_apereances.append(1)
            elements.append(lst[i])
    
    final_list = []

    for i in range(len(elements)):
        j = 0
        while j < 2**number_of_apereances[i]:
            final_list.append(elements[i])
            j += 1


    return elements, number_of_apereances, final_list

# lst = [1,2,2,3,4,4,4,1]

# print(power_replicate(lst))


def group_consecutives(lst):
    """
    This function group similar consecutive elements in a list.
    [1,2,2,3,4,4,4,1] -> [[1], [2, 2], [3], [4, 4, 4], [1]]
    """
    number_of_apereances = [1]
    elements = [lst[0]]

    for i in range(1,len(lst)):
        if lst[i-1] == lst[i]:
            number_of_apereances[-1] += 1
        elif lst[i-1] != lst[i]:
            number_of_apereances.append(1)
            elements.append(lst[i])

    final_list = [[i]*j for i, j in zip(elements, number_of_apereances)]
    return lst, "->", final_list


lst = [1,1,1,2,3,3,3,3,3,4,4,4,4,42,2,2,1,5,6,6,6,6,3,3,3,34,8,8,8,6,6,6,1]

print(group_consecutives(lst))