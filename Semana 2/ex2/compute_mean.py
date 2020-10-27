def compute_mean(first_number, second_number, mean):
    """
    This function computes the mean.
    The first two parameters are the numbers for the calculation.
    The third parameter indicate the type of mean: arithmetic, geometric or harmonic.
    """
    if mean == "A": # Starts the arithmetic mean condition.
        return (first_number+second_number)/2 # Returns the arithmetic mean.

    if mean == "G": # Starts the geometric mean condidion.
        product = first_number*second_number # Store the product of the parameters in a variable.

        if product < 0: # Starts a condition on the negative product.
            return None
        else:
            return (first_number*second_number)**(1/2) # Returns the geometric mean
    
    if mean == "H": # Starts the harmonic mean condition
        if first_number == 0 or second_number == 0: # Starts a condition on wether the parameters are different than 0.
            return None
        else:
            return 2/(1/first_number+1/second_number) # Returns the harmonic mean.
    
    if mean != "A" or "G" or "H": # Starts a condition on wether the mean type is valid.
        return None

