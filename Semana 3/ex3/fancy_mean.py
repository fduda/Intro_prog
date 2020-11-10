def fancy_mean():
    """
    docstring
    """
    print("Please enter the numbers, one in each line")
    number_list= []
    while True:
        number = input()
        if number == "":
            break
        else:
            number_list.append(float(number))

    # if len(number_list) == 0:
    #     return None

    print("The arithmetic mean of the numbers is ", arithmetic_mean(number_list))
    print("The geometric mean of the numbers is ", geometric_mean(number_list))
    print("The harmonic mean of the numbers is ", harmonic_mean(number_list))

def arithmetic_mean(num_lst):
    numerator = 0
    for number in num_lst:
        numerator += number

    return numerator/len(num_lst)


def geometric_mean(num_lst):
    product = 1
    for number in num_lst:
        product *= number
    return product ** (1/len(num_lst))

def harmonic_mean(num_lst):
    list_inverse_numbers = []

    for number in num_lst:  # Creates a list of the inverse numbers.
        list_inverse_numbers.append(1 / number)

    inverse_sum = 0  # Creates a counter that keeps the sum of the inverse.  
    for inverse_number in list_inverse_numbers:
        inverse_sum += inverse_number

    return len(num_lst) / inverse_sum

print(fancy_mean())