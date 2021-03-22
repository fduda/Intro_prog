def power_replicate(lst):
    number_of_appearances = [1]
    elements = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i - 1] == lst[i]:
            number_of_appearances[-1] += 1
        else:
            number_of_appearances.append(1)
            elements.append(lst[i])

    final_lst = []

    for i in range(len(elements)):
        j = 0
        while j < 2**number_of_appearances[i]:
            final_lst.append(elements[i])
            j += 1

    return  final_lst
lst = [1, 2, 2, 3, 4, 4, 4, 1]

print(power_replicate(lst))