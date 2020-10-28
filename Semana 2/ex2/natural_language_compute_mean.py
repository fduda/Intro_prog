import compute_mean as cm

def natural_language_compute_mean(phrase):
    """
    COMENTAR!!
    """
    phrase_in_list = phrase.split(" ")
    numbers_in_list = phrase_in_list[-1].split(",")
    first_number = float(numbers_in_list[0])
    second_number = float(numbers_in_list[1])
    
    if "arithmetic" in phrase:
        return first_number, second_number, cm.compute_mean(first_number,second_number,"A")

    elif "geometric" in phrase:
        return first_number, second_number, cm.compute_mean(first_number,second_number,"G")
    
    elif "harmonic" in phrase:
        return first_number, second_number, cm.compute_mean(first_number,second_number, "H")

    


