def metro(lst):
    count = 0
    for i in lst:
        count += i[0] - i[-1]
    if count == 0:
        return True
    return False

