def fancy_mean():
    """
    This function receives a series of inputs from the user and
    returns the three types of mean: arithmetic, geometric and harmonic.
    """

    print("Please enter the numbers, one in each line: ")
    numbers_list = []
    while True:
        number = input()
        if number == "":
            break
        else:
            numbers_list.append(float(number))
    if numbers_list == []:
        return None

    print("The arithmetic mean of the numbers is {}" \
          .format(arithmetic_mean(numbers_list)))
    print("The geometric mean of the numbers is {}". \
          format(geometric_mean(numbers_list)))
    print("The harmonic mean of the numbers is {}". \
          format(harmonic_mean(numbers_list)))


def arithmetic_mean(num_lst):
    """
    This function receives a list of numbers and calculates the 
    arithmetic mean.
    """
    numerator = 0

    for number in num_lst:
        numerator += number  # Adds all the numbers into one variable.

    return numerator / len(num_lst)


def geometric_mean(num_lst):
    """
    This function receives a list of numbers and calculates the 
    geometric mean.
    """
    product = 1
    for number in num_lst:  # Multiply all the numbers into one variable.
        product *= number
    return product ** (1 / len(num_lst))


def harmonic_mean(num_lst):
    """
    This function receives a list of numbers and calculates the 
    harmonic mean.
    """
    list_inverse_numbers = []

    for number in num_lst:  # Creates a list of the inverse numbers.
        list_inverse_numbers.append(1 / number)

    inverse_sum = 0  # Creates a counter that keeps the sum of the inverse.  
    for inverse_number in list_inverse_numbers:
        inverse_sum += inverse_number

    return len(num_lst) / inverse_sum


def is_palindrome(lst):
    """
    This function checks if a list is a palindrome. That is, if
    it can be read backwards and still the same list.
    """
    # The next 2 lines states that every list with zero or one
    # is a palindrome
    if lst == [] or len(lst) == 1:
        return True

    reversed_lst = []  # Creates a new list for comparison
    for i in reversed(lst):  # Reverse the input list and add the elements
        reversed_lst.append(i)  # backwards.

    if reversed_lst == lst:  # Compares the input list with the reversed list.
        return True
    else:
        return False


def lucky_tosses(lst):
    """""
    This function receives a list of coin tosses represented by 0 and 1. Then
    it calculates the percentage of each type of result in relation to the
    total. Calculates the longest streak of the same result and how many
    streaks longer than 5.
    """""
    # The next block counts how many of each result.
    counter_zero = 0
    counter_one = 0
    for i in lst:
        if i == 0:
            counter_zero += 1
        elif i == 1:
            counter_one += 1
    # The next block calculates the probability of each outcome.
    probability_zero = 100 * counter_zero / len(lst)
    probability_one = 100 * counter_one / len(lst)
    seq_bigger_than_five = greater_than_five(lst)
    max_seq = max_sequence(lst)

    return [probability_one, probability_zero, seq_bigger_than_five, max_seq]


def max_sequence(lst):
    """
    This function receives a list of numbers and calculates the longest
    streak of the same number.
    """
    # Creates a variable for the current number and one for the highest streak.
    counter_maximum = 1
    counter_current = 1

    # The next block compares two elements in the list, if they are the same
    # it adds one to the maximum streak, if not, reset the maximum streak.
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            counter_current += 1
        else:
            if counter_current > counter_maximum:
                counter_maximum = counter_current
            counter_current = 1

    return counter_maximum


def greater_than_five(lst):
    """
    This function receives a list of numbers and returns how many
    streaks of the same number are longer than 5.
    """
    seq_counter = 0
    counter_current = 1
    # The next block compares two elements in the list, if they are the same
    # adds one to the counter, when the currentcounter gets to five, 
    # adds one to the sequence counter, then, resets the current counter.
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            counter_current += 1
        else:
            if counter_current >= 5:
                seq_counter += 1
            counter_current = 1

    return seq_counter


def cumulative_distribution(num_list, value_list):
    """""
    This function receives two lists. For each value in the second list it 
    returns the ratio of numbers on the first list that are smaller or
    equal the first number. Then, returns a new list with all the ratios.
    """""
    final_result = []  # Creates the list that will be returned with results.
    for value in value_list:
        counter = 0  # Counts how many elements in num_list are smaller or equal
        # each element in value_list.
        for number in num_list:
            if number <= value:
                counter += 1
        # The next line appends the division between the counter and the list
        # lenght to final_result.
        final_result.append(counter / len(num_list))
    return final_result


def equal_product_pairs(n):
    """""
    This function receives an integer and returns all the pairs of integers
    that results in n when multiplied.
    """""
    # Generates a list from 2 to n.
    numbers_list = list(range(2, n + 1))
    intermediate_list = []
    final_result_list = []
    # The following loop scans through numbers_list and checks if two
    # numbers gets n as a multiplication. If so, adds the pair to intermediate
    # list.
    for first_number in numbers_list:
        for second_number in numbers_list:
            if first_number * second_number == n:
                pair = [[first_number, second_number]]
                intermediate_list.extend(pair)
    # The next block appends all the pairs, without repetition,
    # to the final list.
    if len(intermediate_list) % 2 == 0:
        final_result_list = intermediate_list[0:int(len(intermediate_list) / 2)]
    elif len(intermediate_list) % 2 != 0:
        final_result_list = \
            intermediate_list[0:int(len(intermediate_list) // 2 + 1)]

    return final_result_list


def pascal_triangle(n):
    """
    This function receives an integer n and prints the first n lines
    of the Pascal's Triangle.
    """
    # The first two if blocks build the first two lines of the triangle.
    # We need at least two lines in order to compare the elements.
    if n == 1:
        pascal_list = [[1]]
    elif n == 2:
        pascal_list = [[1], [1, 1]]
    elif n >= 3:
        pascal_list = [[1], [1, 1]]
        # The next loop creates a a new line,
        # which already starts with the number 1.
        for i in range(2, n):
            new_line = [1]
            counter = 1
            # The next loop compare two subsequent elements, adds them and
            # appends the result to the new line.
            while counter <= i - 1:
                new_number = pascal_list[i - 1][i - counter] + \
                             pascal_list[i - 1][i - counter - 1]
                new_line.append(new_number)
                counter += 1
            new_line.append(1)  # Adds the last number 1 to the line.
            pascal_list.append(new_line)  # Adds the new line and begins a new.
    return pascal_list
