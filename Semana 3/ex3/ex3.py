def fancy_mean():
    """
    docstring
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
    numerator = 0
    for number in num_lst:
        numerator += number

    return numerator / len(num_lst)


def geometric_mean(num_lst):
    product = 1
    for number in num_lst:
        product *= number
    return product ** (1 / len(num_lst))


def harmonic_mean(num_lst):
    list_inverse_numbers = []

    for number in num_lst:  # Creates a list of the inverse numbers.
        list_inverse_numbers.append(1 / number)

    inverse_sum = 0  # Creates a counter that keeps the sum of the inverse.  
    for inverse_number in list_inverse_numbers:
        inverse_sum += inverse_number

    return len(num_lst) / inverse_sum


def is_palindrome(lst):
    """
    docstring
    """

    if lst == [] or len(lst) == 1:
        return True

    reversed_lst = []
    for i in reversed(lst):
        reversed_lst.append(i)

    if reversed_lst == lst:
        return True
    else:
        return False


def lucky_tosses(lst):
    """""
    write your code here
    """""
    counter_zero = 0
    counter_one = 0
    for i in lst:
        if i == 0:
            counter_zero += 1
        elif i == 1:
            counter_one += 1

    probability_zero = 100 * counter_zero / len(lst)
    probability_one = 100 * counter_one / len(lst)
    seq_bigger_than_five = greater_than_five(lst)
    max_seq = max_sequence(lst)

    return [probability_one, probability_zero, seq_bigger_than_five, max_seq]


def max_sequence(lst):
    counter_maximum = 1
    counter_current = 1

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            counter_current += 1
        else:
            if counter_current > counter_maximum:
                counter_maximum = counter_current
            counter_current = 1

    return counter_maximum


def greater_than_five(lst):
    seq_counter = 0
    counter_current = 1
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
    write your code here
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
    write your code here
    """""
    numbers_list = list(range(2, n + 1))
    intermediate_list = []
    final_result_list = []

    for first_number in numbers_list:
        for second_number in numbers_list:
            if first_number * second_number == n:
                pair = [[first_number, second_number]]
                intermediate_list.extend(pair)

    if len(intermediate_list) % 2 == 0:
        final_result_list = intermediate_list[0:int(len(intermediate_list) / 2)]
    elif len(intermediate_list) % 2 != 0:
        final_result_list = \
            intermediate_list[0:int(len(intermediate_list) // 2 + 1)]

    return final_result_list


def pascal_triangle(n):
    """
    docstring
    """
    if n == 1:
        pascal_list = [[1]]
    elif n == 2:
        pascal_list = [[1], [1, 1]]
    elif n >= 3:
        pascal_list = [[1], [1, 1]]
        for i in range(2, n):
            new_line = [1]
            counter = 1
            while counter <= i - 1:
                new_number = pascal_list[i - 1][i - counter] + \
                             pascal_list[i - 1][i - counter - 1]
                new_line.append(new_number)
                counter += 1
            new_line.append(1)
            pascal_list.append(new_line)
    return pascal_list
