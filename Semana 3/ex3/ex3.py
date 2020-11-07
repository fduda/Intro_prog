def fancy_mean():
    """
    docstring
    """

    numbers_list_string = [] # Creates a list for numbers in string type.
    numbers_list_float = [] # Creates a list for numbers in float type.

    # The next line asks the user for the fisrt number.
    first_number_input = input("Please enter the numbers, one in each line: \n") 

    
    if first_number_input == "": # Returns None if the user doesn't input a number.
        return None

    # The next line adds the first number as a string.
    numbers_list_string.append(first_number_input) 

    # The next block is to keep asking the user for the numbers, until he
    # inputs "". Also adds the rest of the numbers as strings to the list.
    while True:
        rest_of_numbers_input = input()
        if rest_of_numbers_input == "":
            break
        else:
            numbers_list_string.append(rest_of_numbers_input)

    # The next loop converts the strings in the list to floats.
    for string_number in numbers_list_string:
        numbers_list_float.append(float(string_number))

    # The next block calculates the arithmetic mean.
    numerator = 0 # Starts a counter.
    for number in numbers_list_float:
        numerator += number

    arithmetic_mean = numerator/len(numbers_list_float)

    # The next block calculates the geometric mean.
    product = 1 # This counter has to start at 1 so the product wont be zero.
    for number in numbers_list_float:
        product *= number

    geometric_mean = product**(1/len(numbers_list_float))

    # The next block calculates the harmonic mean.
    list_inverse_numbers = []
    
    for number in numbers_list_float: # Creates a list of the inverse numbers.
        list_inverse_numbers.append(1/number)

    inverse_sum = 0 # Creates a counter that keeps the sum of the inverse of 
    for inverse_number in list_inverse_numbers:
        inverse_sum += inverse_number

    harmonic_mean = len(numbers_list_float)/inverse_sum

    print("The arithmetic mean of the numbers is {}".format(arithmetic_mean))
    print("The geometric mean of the numbers is {}".format(geometric_mean))
    print("The harmonic mean of the numbers is {}".format(harmonic_mean))
    

def is_palindrome(lst):
    """
    docstring
    """
    
    if lst == [] or len(lst) == 1:
        return True

    reversed_lst =[]
    for i in reversed(lst):
        reversed_lst.append(i)

    if reversed_lst == lst:
        return True
    else:
        return False

