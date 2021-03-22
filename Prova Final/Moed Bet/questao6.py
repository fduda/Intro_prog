def transpose(mat):
    transp = []
    for i in range(len(mat[0])):
        transp.append([])

    for i in range(len(mat[0])):
        for j in range(len(mat)):
            transp[i].append(mat[j][i])
    return transp


# [[1,2,3],[4,5,6],[7,8,9]]

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
