def argmin(a,start):
    index = start
    for i in range(start+1, len(a)):
        if a[i] < a[index]:
            index = i
    return index

def sort(a):
    for i in range(len(a)):
        small = argmin(a,i)
        a[i] , a[small] = a[small], a[i]

a = [56, 12, 34, 77, 35, 34]

sort(a)
