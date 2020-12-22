import random as rd

def binary_search(lst, num):
    # The number doesn't exist in an empty list
    if len(lst) == 0:
        return False
    # The median index of the current list
    m = len(lst)//2
    # if the number we are looking for is larger than the search-
    # list in it's median index- look right
    if num > lst[m]:
        return binary_search(lst[m+1:], num)
    # if the number we are looking for is smaller than the search-
    # list in it's median index- look left
    if num < lst[m]:
        return binary_search(lst[:m], num)
    # if the number isn't smaller & isn't larger - it's equal
    return True





lst = []

# while len(lst) < 20:
#     lst.append(rd.randrange(10))
#     lst.sort()
# print(lst)


print(binary_search([1,2,3,4,5,5,6,6,8,8,9,10],7))  #len(lst) = 12