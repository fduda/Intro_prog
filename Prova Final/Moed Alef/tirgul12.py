from typing import List


def prime_generator():
    i = 2
    while True:
        if is_prime(i) == True:
            yield i
        i+=1
            

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

x = prime_generator()
for i in range(10):
    print(next(x))
