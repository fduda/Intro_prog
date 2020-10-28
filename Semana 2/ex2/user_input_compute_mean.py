import compute_mean as cm # Import the compute_mean file with the "cm" prefix as a shortcut.

def user_input_compute_mean():
    """
    This function asks the user to imput two numbers, then asks the user to input the mean type he wants to calculate.
    Then, the function calculates the result and prints it.
    """
    
    # The following block recieves the users input as a string, separates both numbers in a list,
    # and stores each index of the list in a different variable as floats.
    user_numbers = input("Please enter two numbers, x and y: ")
    user_numbers_list = user_numbers.split(" ")
    first_number = float(user_numbers_list[0])
    second_number = float(user_numbers_list[1])

    mean_type = input("Please enter (A)rithmetic, (G)eometric or (H)armonic: ") # Stores the mean type as a variable

    # The next block uses the function created in the file 'compute_mean' to calculate different kinds of mean.
    # Each if statement execute the 'compute_mean' function and stores the result in the variable 'mean'.

    if mean_type == "A":
        mean_type = "arithmetic" # Changes the variable 'mean_type' to the string 'arithmetic' to be used later.
        mean = cm.compute_mean(first_number, second_number, "A")

    elif mean_type == "G":
        mean_type = "geometric" # Changes the variable 'mean_type' to the string 'geometric' to be used later.
        mean = cm.compute_mean(first_number,second_number, "G")

    elif mean_type == "H":
        mean_type = "harmonic" # Changes the variable 'mean_type' to the string 'harmonic' to be used later.
        mean = cm.compute_mean(first_number,second_number, "H") 
    
    # The next line prints the result using the 'format' function to better organize the string.
    print("The {} mean of {} and {} is {}".format(mean_type, first_number, second_number, mean)) 

