def factorial(n):
    """
    docstring
    """
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(6))