def shrink(lst):
    res = []
    ind = 0
    res.append(lst[0])

    for j in range(1,len(lst)):
        if lst[j] * res[ind] > 0:
            res[ind] += lst[j]
        else:
            ind += 1
            res.append(lst[j])
    return res





