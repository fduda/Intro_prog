# def foo1(lst):
#     if len(lst) == 0:
#         return []
    
#     return [lst[-1]]+foo1(lst[:-1])


lst = [1,4,2,"a", 8,5,"c"]

def foo2(lst):
    if len(lst) == 0:
        return []
    return [lst[-1] + foo2(lst[:-1])]