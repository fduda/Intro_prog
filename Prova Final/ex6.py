def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

def list_inverter(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + list_inverter(lst[:-1])

def is_palindrome(lst):
    if lst == list_inverter(lst):
        return True
    else:
        return False

def sum_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_digits(n//10)


def convert_binary(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return int(str(convert_binary(n//2)) + str(n%2))

def nested_list_sum(lst):
    final_sum = 0

    for i in lst:
        if type(i) == list:
            final_sum += nested_list_sum(i)
        elif type(i) == float or type(i) == int:
            final_sum += i
    return final_sum

lst = [1,2,[[[3,4,[1],[2],2],[[[5,[[[[6]]]]]],[1,2,4]],[[10]]]],1]

print(nested_list_sum(lst))