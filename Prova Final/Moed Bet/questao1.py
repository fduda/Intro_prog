def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def g(n):
    for i in range(2, n+1):
        d = n - i
        if is_prime(d) == True and is_prime(i) == True:
            return d, i


print(g(34))


