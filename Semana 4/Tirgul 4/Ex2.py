def return_max_element_location(lst):
    """
    docstring
    """
    same_lst = lst[:]
    lst.sort()
    max_element = lst[len(lst)-1]
    location = same_lst.index(max_element)
    return location

print(return_max_element_location([1,2,5,2,3,2,5,12,2,3,6,7,8,8,6,5,2,3,12]))


