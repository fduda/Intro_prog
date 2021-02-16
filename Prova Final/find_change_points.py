def find_change_point(lst):
    max_element = max(lst)
    min_element = min(lst)

    if max_element > lst[0]:
        for index, element in enumerate(lst):
            if element == max_element:
                return index
    
    if min_element < lst[0]:
        for index, element in enumerate(lst):
            if element == min_element:
                return index
    

lst1 = [1, 2.3, 5, 4, -2.1 -5]
lst2 = [12, 9, 3, 1.1, 0, 4.2]

print(find_change_point(lst1))