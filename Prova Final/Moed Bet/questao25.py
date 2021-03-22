def sum_lists(lst):
    final_sum = 0

    for i in lst:
        if type(i) == list:
            final_sum += sum_lists(i)
        elif type(i) == float or type(i) == int:
            final_sum += i

    return final_sum


print(sum_lists([2, 5, [1, 9, 3], [2], [3,[4, 1]]]))
