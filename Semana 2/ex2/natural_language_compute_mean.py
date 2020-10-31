import compute_mean as cm  # Import the compute_mean file with the "cm" prefix as a shortcut.


def natural_language_compute_mean(phrase):
    """
    This function receives a phrase that informs the program two different numbers and what kind of mean to calculate.
    Then, calculates the specific mean using those two numbers.
    """

    # The following block is built to store both numbers used to calculate the mean in two different variables

    phrase_in_list = phrase.split(" ")  # Creates a list by separating the phrases on every space.
    numbers_in_list = phrase_in_list[-1].split(",")  # Gets the last item on the previous list and splits it into two numbers. Stores it in a new list.
    first_number = float(
        numbers_in_list[0])  # Creates a variable that stores the first element of the list above as the first number.
    second_number = float(
        numbers_in_list[1])  # Creates a variable that stores the second element of the list above as the second number.

    # The next block uses the function created in the file 'compute_mean' to calculate different kinds of mean.
    # Each if statement returns the both numbers followed by the mean calculated.

    if "arithmetic" in phrase:  # Starts this conditional if the word 'arithmetic' is found in the phrase.
        return first_number, second_number, cm.compute_mean(first_number, second_number, "A")

    elif "geometric" in phrase:  # Starts this conditional if the word 'geometric' is found in the phrase.
        return first_number, second_number, cm.compute_mean(first_number, second_number, "G")

    elif "harmonic" in phrase:  # Starts this conditional if the word 'harmonic' is found in the phrase.
        return first_number, second_number, cm.compute_mean(first_number, second_number, "H")
