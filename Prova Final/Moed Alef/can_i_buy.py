def can_i_buy(n):
    if n < 7:
        return False

    if (n%7 == 0) or (n%9 == 0) or (n%11 == 0):
        return True
    
    if can_i_buy(n-7) == True:
        return True
    if can_i_buy(n-9) == True:
        return True
    if can_i_buy(n-11) == True:
        return True
    
    return False

print(can_i_buy(24))

def can_i_buy_2(n):

    for s7 in range(n//7):
        for s9 in range(n//9):
            for s11 in range(n//11):
                if s7*7 + s9*9 + s11*11 == n:
                    return True
    return False

print(can_i_buy_2(63))