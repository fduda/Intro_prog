def palindrome(lst):
    inverted_list = []

    if len(lst) == 0 or len(lst) == 1:
        return True

    for i in range(len(lst)-1,-1,  -1):
        inverted_list.append(lst[i])
    
    if lst == inverted_list:
        return True
    return False


def list_packer(lst):
    number_of_apearences = [1]
    elements = [lst[0]]

    for i in range(1,len(lst)):
        if lst[i-1] == lst[i]:
            number_of_apearences[-1] += 1
        else:
            number_of_apearences.append(1)
            elements.append(lst[i])
    
    return [[i]*j for i,j in zip(elements, number_of_apearences)]


def lucky_tosses(lst):
    packed_list = list_packer(lst)
    heads_percentage = lst.count(1)*100/len(lst)
    tails_percentage = lst.count(0)*100/len(lst)

    counter_seq = 0
    for i in packed_list:
        if len(i) > 4:
            counter_seq += 1
    
    longes_seq = 0
    for i in packed_list:
        if len(i) > longes_seq:
            longes_seq = len(i)

    return [heads_percentage, tails_percentage, counter_seq, longes_seq]


# print(lucky_tosses([1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1]))
# print(lucky_tosses([1,1,0,0,1,1,1,1,0,0,0,1,1,1]))


def cumulative_distribution(num_list, value_list):
    final_list = []

    for value in value_list:
        counter = 0
        for number in num_list:
            if number <= value:
                counter += 1
        final_list.append(counter/len(num_list))

    return final_list


# print(cumulative_distribution([1, 2, 3, 4],[0, 0.5, 1, 2, 3, 4]))

def equal_product_pairs(n):
    divisors = [i for i in range(1,int(n/2)+1) if n%i == 0]
    inter_list = []

    for i in divisors:
        for j in divisors:
            if i*j == n:
                inter_list.append([i,j])



    return [inter_list[i] for i in range(0,int(len(inter_list)/2)+1)]

# print(equal_product_pairs(36))

def pascal(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1,1]]
    final_list = [[1], [1,1]]
    line_number = 3
    while line_number <= n:
        last_line = final_list[-1]
        new_line = [1]
        for i in range(1, len(last_line)):
            new_line.append(last_line[i-1]+last_line[i])
        new_line.append(1)
        final_list.append(new_line)
        line_number += 1
    return final_list

print(pascal(31))

# def pascal_triangle(n):
#     if n == 1:
#         pascal_list = [[1]]
#     elif n == 2:
#         pascal_list = [[1], [1, 1]]
#     elif n >= 3:
#         pascal_list = [[1], [1, 1]]
#         for i in range(2, n):
#             new_line = [1]
#             counter = 1
#             while counter <= i - 1:
#                 new_number = pascal_list[i - 1][i - counter] + pascal_list[i - 1][i - counter - 1]
#                 new_line.append(new_number)
#                 counter += 1
#             new_line.append(1)  # Adds the last number 1 to the line.
#             pascal_list.append(new_line)  # Adds the new line and begins a new.
#     return pascal_list