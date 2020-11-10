def lucky_tosses(lst):
    """""
    write your code here
    """""
    counter_seq = 0
    counter_seq_max = 0

    for i in lst:
        if lst[i] == lst[i+1]:
            counter_seq += 1
        elif lst[i] != lst[i+1]:
            counter_seq_max = counter_seq

    return counter_seq_max


print(lucky_tosses([1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1]))



def ratio(lst):
    """
    docstring
    """
    counter_zero = 0
    counter_one = 0
    for i in lst:
        if i == 0:
            counter_zero +=1
        elif i == 1:
            counter_one += 1

        probability_zero = 100*counter_zero/len(lst)
        probability_one = 100*counter_one/len(lst)
    return probability_zero, probability_one

# [1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1]