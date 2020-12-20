def factorial(n):
    """
    docstring
    """
    if n == 0:
        return 1
    return n*factorial(n-1)


def is_palindrome(lst):
    if lst == return_reverse(lst):
        return True
    else:
        return False

def return_reverse(lst):
    if len(lst) == 0:
        return lst
    elif len(lst) == 1:
        return lst
    
    return [lst[-1]] + return_reverse(lst[:-1])



def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_of_digits(n//10)


    


def convert_decimal_to_binary(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return int(str(convert_decimal_to_binary(n//2))+str(n%2))


def convert_binary(n):
    print(convert_decimal_to_binary(n))
