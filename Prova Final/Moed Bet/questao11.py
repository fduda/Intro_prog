def group(lst):
    number_of_appearances = [1]
    elements = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i - 1] == lst[i]:
            number_of_appearances[-1] += 1
        else:
            number_of_appearances.append(1)
            elements.append(lst[i])

    final_list = [[i]*j for i,j in zip(elements,number_of_appearances)]
    return final_list

def compress(lst):
    grouped_lst = group(lst)
    final_lst = [(grouped_lst[i][0], len(grouped_lst[i])) for i in range(len(grouped_lst))]
    return final_lst

print(compress(["a", "a", "b", "b", "b", "c", "a", "a"]))