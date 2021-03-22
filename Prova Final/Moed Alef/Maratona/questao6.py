def transpose(lst):
    res = []
    for i in range(len(lst[0])):
        res.append([])
    for i in range(len(lst[0])):
        for j in lst:
            res[i].append(j[i])
    return res
arr = [[1,2,3],[4,5,6],[7,8,9]]

print(transpose(arr))