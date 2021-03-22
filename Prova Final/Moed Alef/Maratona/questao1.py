def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def g(n):
    for i in range(2, n+1):
        d = n-i
        if prime(i) == True and prime(d) == True:
            return i,d
            