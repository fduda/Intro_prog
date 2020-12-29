def factorial(n):
    """
    This function returns the factorial of a number.
    """
    if n == 0:  # Stopping condition.
        return 1
    return n*factorial(n-1)  # Recursive step.


def is_palindrome(lst):
    """
    This function recieves a list and verifies if it is a palindrome,
    that is, if the list backwards is equal to the original list.
    """
    # The next block compares the list with the list's backwards version.
    if lst == return_reverse(lst): 
        return True
    else:
        return False

def return_reverse(lst):
    """
    This function reverses a list.
    """
    if len(lst) == 0:  # Stopping condition.
        return lst
    elif len(lst) == 1:
        return lst
    
    return [lst[-1]] + return_reverse(lst[:-1])  # Recursive step.



def sum_of_digits(n):
    """
    This function returns the sum of all the numbers digits.
    """
    if n == 0:  # Stopping condition.
        return 0
    return n%10 + sum_of_digits(n//10)  # Recursive step.


    


def convert_decimal_to_binary(n):
    """
    This function converts a decimal number into its binary version.
    """
    if n == 1:  # Stopping condition.
        return 1
    if n == 0:  # Stopping condition.
        return 0
    return int(str(convert_decimal_to_binary(n//2))+str(n%2))  # Recursive step.


def convert_binary(n):
    """
    This is an auxiliary function.
    It prints the result of another function.
    """
    print(convert_decimal_to_binary(n))


def nested_list_sum(lst):
    """
    This function sums all the elements in a list of lists.
    """
    final_sum = 0  # Starts a counter.
    for i in lst:  # Loops through the outer list.
        if type(i) == list:  
            final_sum += nested_list_sum(i)  # If the element is a list, run the function through recursion.
        elif type(i) == float or type(i) == int:
            final_sum += i  # Adds the element's value.
    return final_sum  # Return result.



def choose_branches(n, picker):
    """
    This functions transforms all the possibilities into a tree.
    """
    if picker == "first_player":
        if n == 1:
            p1 = 1
            p2 = 2
        else:
            if n % 3 == 0:
                p1 = n+1
                p2 = n+1
            # elif n % 3 == 1:
            #     p1 = 4
            #     p2 = n+1
            else:
                r = n % 3
                p1 = r
                p2 = r + 3
                if p2>4:
                    p2=n+1

        # The next block returns three branches for every number of coins.
        left = n - p1
        center = -1
        right = n - p2

        # If a branch is negative, it is not considered as a possibility.

        return left, center, right

    if picker == "second_player":
        left = n - 1
        center = n - 2
        right = n - 4
        return left, center, right


def possibilities_counter(n, players, counter=0, p=0):
    """
    This function goes through the possibility tree and counts how many possibilities 
    there are in total.
    """
    

    picker = players[p]  # Sets who's turn it is.

    if n<0:
        return counter
    elif n==0:
        counter += 1  # Counts the number of possibilities.
        return counter
    else:
        left, center, right = choose_branches(n, picker)
       
    

    p = (p+1) % 2  # Alternates between the players.
    picker = players[p]

    # The next block counts the possibilities of each branch.
    counter = possibilities_counter(left, players=players, counter=counter, p=p)
    counter = possibilities_counter(center, players=players, counter=counter, p=p)
    counter = possibilities_counter(right, players=players, counter=counter, p=p)
    
    return counter


def make_game(players, n):
    """
    This function plays the game and based on the number of players and the 
    coins on the table.
    """

    if n % 3 == 0:
        winner = players[1]
        players = players[::-1]
    else:
        winner = players[0]

    possibilities = possibilities_counter(n, players=players, counter=0, p=0)
    
    return winner, possibilities  # Returns the winner and the number of possibilities.


def coin_pick_winner(n):
    """
    This function recieves a number of coins.
    Returns True if the first players wins together with the number of possibilities.
    Returns False if the first players loses together with the number of possibilities.
    """
    players = ["first_player", "second_player"]
    winner, possibilities = make_game(players, n)

    if winner == "first_player":
        return (True, possibilities)
    else:
        return (False, possibilities)