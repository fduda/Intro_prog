def lucky_tosses(lst):
    """""
    write your code here
    """""
    counter_zero = 0
    counter_one = 0
    for i in lst:
        if i == 0:
            counter_zero +=1
        elif i == 1:
            counter_one += 1

    probability_zero = 100*counter_zero/len(lst)
    probability_one = 100*counter_one/len(lst)
    seq_bigger_than_five = greater_than_five(lst)
    max_seq = max_sequence(lst)
    return [probability_one, probability_zero, seq_bigger_than_five, max_seq]


# [1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1]
# [1,1,0,0,1,1,1,1,0,0,0,1,1,1]
def max_sequence(lst):
    counter_maximum = 1
    counter_current = 1

    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            counter_current += 1
        else:
            if counter_current > counter_maximum:
                counter_maximum = counter_current
            counter_current = 1
    return counter_maximum

def greater_than_five(lst):
    seq_counter = 0
    counter_current = 1
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            counter_current += 1
        else:
            if counter_current >=5 :
                seq_counter += 1
            counter_current = 1
        
    return seq_counter

# print(greater_than_five([1,1,0,0,1,1,1,1,0,0,0,1,1,1]))

print(lucky_tosses([1,1,0,0,1,1,1,1,0,0,0,1,1,1]))