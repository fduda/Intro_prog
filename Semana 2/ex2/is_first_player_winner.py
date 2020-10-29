import compute_mean as cm  # Import the compute_mean file with the "cm" prefix as a shortcut.



def is_first_player_winner(pofn, posn, ptfn, ptsn):
    """
    This function takes four parameters, calculates all the means between the first two and the last two.
    Then, it stores the difference between the mean calculated with the first two numbers and with the last two numbers. Does it for all three means.
    Sums the results, analyses the signal and returns True of False.
    """

    # The parameters name are a written in a shorter way, where "pofn" means player_one_first_number,
    # "posn" means player_one_second_number, "ptfn", means player_two_first_number, and "ptsn" means player_two_second_number.
    # This is abbreviation was made in order to keed the code cleaner and shorter.
    
    # The next block calculates the difference between each mean, with each players numbers.
    difference_arithmetic_mean = cm.compute_mean(pofn, posn, "A") - cm.compute_mean(ptfn, ptsn, "A")
    difference_geometric_mean = cm.compute_mean(pofn, posn, "G") - cm.compute_mean(ptfn, ptsn, "G")
    difference_harmonic_mean = cm.compute_mean(pofn, posn, "H") - cm.compute_mean(ptfn, ptsn, "H")
    
    # The next line sums all the differences.
    sum_of_means = difference_arithmetic_mean + difference_geometric_mean + difference_harmonic_mean

    # The next block analyses the signal of sum_of_means and returns True of False depending on it.
    if sum_of_means >= 0:
        return True
    else:
        return False
    print("Diff arith mean: {}, Diff geom mean {}, Diff harm mean: {}, Sum: {}".format(difference_arithmetic_mean, difference_geometric_mean, difference_harmonic_mean, sum_of_means))  