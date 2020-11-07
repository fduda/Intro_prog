def fancy_mean():
    """
    docstring
    """
    numbers_list_string = []
    numbers_list_float = []

    print("Please enter the numbers, one in each line: ")
    
    while True:
        number_input = input()
        if number_input == "":
            break
        else:
            numbers_list_string.append(number_input)
    
    if numbers_list_string == []:
        return None

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

    print(harmonic_mean)


print(fancy_mean())
        