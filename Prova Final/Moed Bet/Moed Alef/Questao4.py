def last_index(lst, n):
    low = 0
    high = len(lst) - 1
    mid = (low + high) // 2

    while low <= high:
        if lst[mid] <= n:
            low = mid + 1
            mid = (low + high) // 2

        else:
            high = mid - 1
            mid = (low + high) // 2
    if lst[mid] == n:
        return mid
    return False

print(last_index([1,2,2,2,2,2,2,2,2,2,2,3],2))