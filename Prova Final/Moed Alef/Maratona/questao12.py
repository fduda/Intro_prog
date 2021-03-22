# def sum_index(lst):
#     for ind in range(len(lst)):
#         if sum(lst[:int]) == sum(lst[ind + 1:]):
#             return True, ind
#     return False

def sum_index2(lst):
    for i in range(len(lst)):
        sum_before = sum(lst[:i])
        sum_after = sum(lst[i+1:])
        if sum_before == sum_after:
            return True, i
    return False

lst = [1,2,3,12,6]
print(sum_index2(lst))