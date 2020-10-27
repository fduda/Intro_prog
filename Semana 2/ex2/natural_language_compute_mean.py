def natural_language_compute_mean(phrase):
    """
    COMENTAR!!
    """
    first_number = int(phrase[-3])
    second_number = int (phrase[-1])
    
    if "arithmetic" in phrase:
        return first_number, second_number, (first_number+second_number)/2

    elif "geometric" in phrase:
        product = first_number*second_number
        if product <0:
            return None
        else:
            return first_number, second_number, (first_number*second_number)**(1/2)
    
    elif "harmonic" in phrase:
        if first_number == 0 or second_number == 0: # Starts a condition on wether the parameters are different than 0.
            return None
        else:
            return first_number, second_number, 2/(1/first_number + 1/second_number)


    

# print(natural_language_compute_mean("Compute arithmetic mean of 5,7"))
# print(natural_language_compute_mean("Compute geometric mean of 5,7"))
# print(natural_language_compute_mean("Compute harmonic mean of 5,7"))
print(natural_language_compute_mean("arithmetic mean of 5,7"))