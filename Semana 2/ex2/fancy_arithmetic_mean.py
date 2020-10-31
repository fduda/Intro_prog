def fancy_arithmetic_mean():
    """
    This function calculates the arithmetic mean by asking the user how many numbers he would like to use,
    and then asking the user what numbers he would like to use. Then, calculates the mean and prints it.
    """

    number_of_numbers = int(input("Please enter a number of numbers (1-5): "))  # Asks the user how many numbers.

    if number_of_numbers > 5 or number_of_numbers < 0:
        # If the user puts a number bigger than 5 or a negative number as an amount of numbers, prints a message to
        # the user.
        print("The number you entered is not between 1 and 5, goodbye!")

    # Each block in the next lines works pretty much the same way.
    # Depending on the amount of numbers chosen by the user, the script starts a different elif statement.
    # On each elif statement, the script asks the user what numbers he would like to calculate the mean.
    # Then, the block calculates the mean and prints the result to the user with a message.
    # The "format" method is used to better organize the code.
    elif number_of_numbers == 1:
        print("Please enter the numbers, one in each line ")
        n_1 = int(input())
        mean = n_1
        print("The arithmetic mean of the numbers is {}".format(mean))

    elif number_of_numbers == 2:
        print("Please enter the numbers, one in each line ")
        n_1 = int(input(""))
        n_2 = int(input(""))
        mean = (n_1 + n_2) / 2
        print("The arithmetic mean of the numbers is {}".format(mean))

    elif number_of_numbers == 3:
        print("Please enter the numbers, one in each line ")
        n_1 = int(input(""))
        n_2 = int(input(""))
        n_3 = int(input(""))
        mean = (n_1 + n_2 + n_3) / 3
        print("The arithmetic mean of the numbers is {}".format(mean))

    elif number_of_numbers == 4:
        print("Please enter the numbers, one in each line ")
        n_1 = int(input(""))
        n_2 = int(input(""))
        n_3 = int(input(""))
        n_4 = int(input(""))
        mean = (n_1 + n_2 + n_3 + n_4) / 4
        print("The arithmetic mean of the numbers is {}".format(mean))

    elif number_of_numbers == 5:
        print("Please enter the numbers, one in each line ")
        n_1 = int(input(""))
        n_2 = int(input(""))
        n_3 = int(input(""))
        n_4 = int(input(""))
        n_5 = int(input(""))
        mean = (n_1 + n_2 + n_3 + n_4 + n_5) / 5
        print("The arithmetic mean of the numbers is {}".format(mean))


fancy_arithmetic_mean()
