def check_perfect(n):
    lst_divisors = []
    for i in range(1,n+1):
        if n%i == 0 and i != n:
            lst_divisors.append(i)

    if sum(lst_divisors) == n:
        return True
    return False

def get_perfect(n):
    perfect_list = []

    for i in range(1,n+1):
        if check_perfect(i) == True:
            perfect_list.append(i)

    return perfect_list

print(get_perfect(500))