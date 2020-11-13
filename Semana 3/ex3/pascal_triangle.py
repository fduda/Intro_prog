# def pascal_triangle(n):
#     """
#     docstring
#     """
#     if n == 1:
#         pascal_list = [[1]]
#     elif n == 2:
#         pascal_list = [[1],[1,1]]
#     elif n >= 3:
#         pascal_list = [[1],[1,1],[1,2,1]]
#         for i in pascal_list:
#             middle_columns = []
#             for j in range(1,n+1):
#                 return None
#     return pascal_list

# print(pascal_triangle(5))


def list_generator(n):
    return list(range(1,n+1))


# print(list_generator(1))

# def pascal_triangle(n):
#     """
#     docstring
#     """
#     pascal_list = [[1]]
#     for i in range(1,n+1):
#         new_line = []
#         for j in pascal_list:
#             new_line.append(1)
#             new_number = 0
#     return None

# def pascal_triangle(n):
#     """
#     docstring
#     """
    # if n == 1:
    #     pascal_list = [[1]]
    # elif n == 2:
    #     pascal_list = [[1],[1,1]]
    # elif n >= 3:
    #     pascal_list = [[1],[1,1]]
#         while len(pascal_list) <= n:
#             for i in range(2,n+1):
#                 new_line = [1]
#                 for j in pascal_list:
#                     new_number = pascal_list[n+i-5] + pascal_list[n+i-6]
#                     new_line.append(new_number)
#                 new_line.append(1)
#                 break
#             pascal_list.append(new_line)

#     return pascal_list

# print(pascal_triangle(4))            

# def pascal_triangle(n):
#     """
#     docstring
#     """
#     if n == 1:
#         pascal_list = [[1]]
#     elif n == 2:
#         pascal_list = [[1],[1,1]]
#     elif n >= 3:
#         pascal_list = [[1],[1,1]]
#         while len(pascal_list) <= n:
#             for i in range(2,n+1):
#                 new_line = [1]
#                 for j in range(1,n+1):
#                     new_number = pascal_list[i-1][i-1]+pascal_list[i-1][i-2]
#                     new_line.append(new_number)
#                 new_line.append(1)
#             pascal_list.append(new_line)
#     return pascal_list

# print(pascal_triangle(3))



# print(pascal_triangle(3))


# pascal_list = [[1],[1,1]]
# print(pascal_list[1])
# print([1]+[1])

def pascal_triangle(n):
    """
    docstring
    """
    if n == 1:
        pascal_list = [[1]]
    elif n == 2:
        pascal_list = [[1],[1,1]]
    elif n >= 3:
        pascal_list = [[1],[1,1]]
        for i in range(2,n):
            new_line = [1]
            counter = 1
            while counter <= i-1:
                new_number = pascal_list[i-1][i-counter]+pascal_list[i-1][i-counter-1]
                new_line.append(new_number)
                counter += 1
            new_line.append(1)
            pascal_list.append(new_line)
    return pascal_list

print(pascal_triangle(12))
