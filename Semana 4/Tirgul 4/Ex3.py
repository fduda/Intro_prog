def max_element_between_lists(lst):
    """
    docstring
    """
    final_list = []
    for i in lst:
        i.sort()
        final_list.append(i[len(i)-1])
    final_list.sort()

    return final_list[len(final_list)-1]

print(max_element_between_lists([[2,5,2,3],[2,6,3,8,7],[3,5,2,9,4,2],[2,3,6,4,12,0,2,3,15]]))