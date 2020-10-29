def fancy_arithmetic_mean():
    """
    docstring
    """
    number_of_numbers = int(input("Please enter a number of numbers (1-5): \n"))

    if number_of_numbers > 5 or number_of_numbers < 0:
        print("The number you entered is not between 1 and 5, goodbye!")

    elif number_of_numbers == 1:
        n_1 = int(input("Please enter the numbers, one in each line \n"))
        mean = n_1
    
    elif number_of_numbers == 2:
        n_1 = int(input("Please enter the numbers, one in each line \n"))
        n_2 = int(input(""))
        mean = (n_1+n_2)/2

    elif number_of_numbers == 3:
        n_1 = int(input("Please enter the numbers, one in each line \n"))
        n_2 = int(input(""))
        n_3 = int(input(""))
        mean = (n_1+n_2+n_3)/3

    elif number_of_numbers == 4:
        n_1 = int(input("Please enter the numbers, one in each line \n"))
        n_2 = int(input(""))
        n_3 = int(input(""))
        n_4 = int(input(""))
        mean = (n_1+n_2+n_3+n_4)/4

    elif number_of_numbers == 5:
        n_1 = int(input("Please enter the numbers, one in each line \n"))
        n_2 = int(input(""))
        n_3 = int(input(""))
        n_4 = int(input(""))
        n_5 = int(input(""))
        mean = (n_1+n_2+n_3+n_4+n_5)/5
        print("The arithmetic mean of the numbers is {}".format(mean))
        
    
    #print("The arithmetic mean of the numbers is {}".format(mean))

fancy_arithmetic_mean()