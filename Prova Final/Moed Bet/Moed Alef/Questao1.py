def find_values(A):
    z = sum([list(item.values()) for item in A],[])
    return {i for i in z if z.count(i) >= 3}


print(find_values([{'f':24,'t':1,'r':1,'e':1},{'fa':24,'ta':24,'ra':33,'ea':12},{'fv':2,'tv':4,'rv':36,'ev':1}]))