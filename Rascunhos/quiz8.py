def g(x, e):
    L = 0
    M = x
    while (M-L>e):
        if 2**((M+L)/2) > x:
            M = (M+L)/2
        else:
            L = (M+L)/2
    return L

print(g(3,0.0000000001))