def sum_index(lst):
    counter = 0
    while counter < len(lst)+1:
        sum_bef = sum(lst[:counter])
        sum_aft = sum(lst[counter+1:])
        if sum_bef == sum_aft:
            return True
        counter += 1
    return False

print(sum_index([1,2,3,12,6]))