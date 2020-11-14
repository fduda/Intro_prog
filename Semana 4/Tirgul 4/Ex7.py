def is_number_in_list(lst,n):
    """
    docstring
    """
    for i in lst:
        if i == n:
            return True
        else:
            return False

print(is_number_in_list([1,2,3,4],3))
