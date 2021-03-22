def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        b = a+b
        a = b-a


fib = fibonacci()

for i in range(10):
    print(next(fib))