def binary_search(lst, n):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (high + low) // 2

        if lst[mid] < n:
            low = mid + 1
        elif lst[mid] > n:
            high = mid - 1
        else:
            return True

    return False


lst_1 = ["microsoft", "blackberry", "cellcom", "apple", "orange", "google"]
lst_2 = ["apple", "banana", "blackberry", "orange", "peach"]


def find_common_names(lst1, lst2):  # lst2 sorted
    res = []

    for i in lst1:
        if binary_search(lst2, i):
            res.append(i)
    return res

print(find_common_names(lst_1,lst_2))