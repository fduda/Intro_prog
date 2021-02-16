def nested_list_sum(lst):
    """
    This function sums all the elements in a list of lists.
    """
    final_sum = 0  # Starts a counter.
    for i in lst:  # Loops through the outer list.
        if type(i) == list:  
            final_sum += nested_list_sum(i)  # If the element is a list, run the function through recursion.
        elif type(i) == float or type(i) == int:
            final_sum += i  # Adds the element's value.
    return final_sum  # Return result.


lst = [2,5,[1,9,3],[2],[3,[4,1]]]

print(nested_list_sum(lst))