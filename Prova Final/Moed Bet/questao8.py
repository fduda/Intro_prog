def shrink(lst):
    res = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i-1] * lst[i] > 0:
            res[-1] += lst[i]
        else:
            res.append(lst[i])
    return res



lst = [2,5,-3,-1,-1,3,-2,-2]

print(shrink(lst))