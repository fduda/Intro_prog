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
        for i in range(2,n+1):
            new_line = []
            for j in pascal_list[1:n+1]:
                new_line.append(1)
                new_number = j[n-i-2]+j[n-i-1]
                new_line.append(new_number)
                # new_line.append(1)

    return pascal_list

print(pascal_triangle(4))            