import time

def is_perfect(n):
    res = []
    for i in range(1, n):
        if n % i == 0:
            res.append(i)

    if sum(res) == n:
        return True
    return False


def get_perfect(n):
    res = []
    for i in range(1, n + 1):
        if is_perfect(i) == True:
            res.append(i)
    return res

start_time = time.time()

print(get_perfect(100000))

print(time.time()-start_time)
