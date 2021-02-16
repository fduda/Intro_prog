def special_triangle(lst):
    n = len(lst)
    if n == 1:
        print(lst)
        return
    if n == 2:
        special_triangle([sum(lst)])
        print(lst)
        return
    if n == 3:
        special_triangle([sum(lst[:2])]+[lst[-1]])
        print(lst)
        return
    
    special_triangle([sum(lst[:2])]+lst[2:-2]+[sum(lst[-2:])])
    print(lst)
    return

special_triangle([12,4,1,2,3,5,2,1,5,2,22,14,14,3])