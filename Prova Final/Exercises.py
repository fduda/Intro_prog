from typing import List


def find_common_names(lst1, lst2):
    size1 = len(lst1)
    size2 = len(lst2)

    i, j = 0, 0
    res = []
    while i < size1 and j < size2:
        if lst1[i] < lst2[j]:
            i += 1
        else:
            if lst1[i] == lst2[j]:
                res.append(lst1[i])
            j += 1
    return res


# a = ['apple', 'blackberry', 'cellcom', 'google', 'microsoft', 'orange']
# b = ['apple', 'banana', 'blackberry', 'orange', 'peach']

# print(find_common_names(a, b))


class Polygon:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add_vertex(self, x, y, i):
        self.x = self.x.insert(i, x)
        self.y = self.y.insert(y, x)

    

def subsets(lst, k):
    if k == 0 or len(lst) == 0:
        return [[]]
    pass

def find_epidemic(lst):
    number_of_appereances = [1]
    elements = [lst[0]]
    for i in range(1,len(lst)):
        if lst[i-1] == lst[i]:
            number_of_appereances[-1] += 1
        elif lst[i-1] != lst[i]:
            number_of_appereances.append(1)
            elements.append(lst[i])
    
    packed_list = [[i]*j for i, j in zip(elements, number_of_appereances)]

    res = [item for item in packed_list if len(item) > 1]
    final_set = {i[0] for i in res}
    return list(final_set)

# lst = ["Zika","Corona","Corona","HIV","Flu","Corona","Corona","Zika",'Flu','Flu',"Corona"]

# print(find_epidemic(lst))

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def gcp(n1, n2):
    divisors_n1 = {i for i in range(1,n1+1) if n1%i == 0}
    divisors_n2 = {i for i in range(1,n2+1) if n2%i == 0}
    
    comon_divisors = divisors_n1.intersection(divisors_n2)
    prime_common_divisors = {i for i in comon_divisors if is_prime(i) == True}
    return max(prime_common_divisors)


def is_perfect(n):
    divisors = [i for i in range(1, n) if n%i ==0]
    if sum(divisors) == n:
        return True
    return False

def get_perfect(n):
    lst = []

    for i in range(2,n):
        if is_perfect(i) == True:
            lst.append(i)

    return lst

print(get_perfect(100))


