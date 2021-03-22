def find(lst, target_num):
    for i in lst:
        for j in lst:
            if i == j:
                break
            if i+j == target_num:
                return True
    return False

lst = [1,2,3,4,1,15,16,12,4,18]

print(find(lst,30))

def find2(lst, num):
    s = 0
    end = len(lst) - 1

    while s != end:
        if lst[s] + lst[end] == num:
            return True, lst[s], lst[end]
        elif lst[s] + lst[end] < num:
            s += 1
        elif lst[s] + lst[end] > num:
            end -= 1
    return False

        