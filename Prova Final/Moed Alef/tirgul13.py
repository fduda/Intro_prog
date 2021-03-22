def permutation(lst):
    if len(lst) <= 1:
        yield lst
    
    else:
        for i in range(len(lst)):
            perms = permutation(lst[:i] + lst[i+1:])
            for p in perms:
                res = [lst[i]] + p
                yield res


p = permutation([1,2,3])
for i in p:
    print(i)