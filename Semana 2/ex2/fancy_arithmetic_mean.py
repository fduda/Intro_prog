def fancy_arithmetic_mean():
    """
    docstring
    """
    number_of_numbers = int(input("Please enter a number of numbers (1-5): \n"))

    if number_of_numbers > 5 or number_of_numbers < 0:
        print("The number you entered is not between 1 and 5, goodbye!")
    else:
        int(input("Please enter the numbers, one in each line \n"))

    #print(number_of_numbers)


fancy_arithmetic_mean()