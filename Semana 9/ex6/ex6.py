def factorial(n):
    """
    This function returns the factorial of a number.
    """
    if n == 0:  # Stopping condition.
        return 1
    return n*factorial(n-1)  # Recursive step.


def is_palindrome(lst):
    """
    This function recieves a list and verifies if it is a palindrome,
    that is, if the list backwards is equal to the original list.
    """
    # The next block compares the list with the list's backwards version.
    if lst == return_reverse(lst): 
        return True
    else:
        return False

def return_reverse(lst):
    """
    This function reverses a list.
    """
    if len(lst) == 0:  # Stopping condition.
        return lst
    elif len(lst) == 1:
        return lst
    
    return [lst[-1]] + return_reverse(lst[:-1])  # Recursive step.



def sum_of_digits(n):
    """
    This function returns the sum of all the numbers digits.
    """
    if n == 0:  # Stopping condition.
        return 0
    return n%10 + sum_of_digits(n//10)  # Recursive step.


    


def convert_decimal_to_binary(n):
    """
    This function converts a decimal number into its binary version.
    """
    if n == 1:  # Stopping condition.
        return 1
    if n == 0:  # Stopping condition.
        return 0
    return int(str(convert_decimal_to_binary(n//2))+str(n%2))  # Recursive step.


def convert_binary(n):
    """
    This is an auxiliary function.
    It prints the result of another function.
    """
    print(convert_decimal_to_binary(n))


def nested_list_sum(lst):
    """
    This function sums all the elements in a list of lists.
    """
    final_sum = 0  # Starts a counter.
    for i in lst:  # Loops through the outer list.
        if type(i) == list:  
            final_sum += nested_list_sum(i)  # If the element is a list, run the function through recursion.
        elif type(i) == float or type(i) == int:
            final_sum += i  # Adds the element's value.
    return final_sum  # Return result.

def coin_pick_winner(n):
    pass
    
    

print(coin_pick_winner(4))
