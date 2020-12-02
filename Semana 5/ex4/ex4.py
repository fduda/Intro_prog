# Template file for dobble
import copy
import random
import time


# 1. Intersect two cards
def cards_intersect(card1, card2):
    """This functions receives two cards and checks if 
    they have a symbol in common
    """
    # The next two lines transform the cards from lists to sets.
    card1_set = set(card1) 
    card2_set = set(card2)
    # The next line gets a list of the symbols in common.
    in_both = list(card1_set.intersection(card2_set))
    return in_both


# 2. Check if card is in deck and remove it
def remove_card(deck, card):
    """This function receives a deck (list of lists) and a
     card (list of words). If the card is in the deck, the 
     function removes it and returns the boolean True, if not, 
     it prints an error message and returns the boolean False.
    """

    deck_set = {frozenset(card) for card in deck}  # New variable in which every card is a set.
    card_to_remove_set = frozenset(card)



    for card_list in deck:
        card_set = set(card_list) # converts every card in the deck into a set.
        if len(card_set.union(card_to_remove_set)) == \
                len(card_to_remove_set):
            deck.remove(card_list) # Removes the card from the orignal deck.
            return True

    # Prints error message and returns the boolean False.
    if card_to_remove_set not in deck_set:
        print("Error! card is not in the deck!")
        return False


# 3. Check if new card matches and add it to the deck
def add_card(deck, card):
    """
    This function receives a deck (list of lists) and a
    card (list of words). If the new card has the same 
    lenght of the cards in the deck, and if it has exactly one 
    common symbol with the other cards in the deck, adds the new card
    to the deck and returns the boolean True. If not, prints an error message
    and returns the boolean False.
    """

    deck_set = {frozenset(card) for card in deck}  # New variable in which every card is a set.
    card_to_add_set = frozenset(card) # New variable in which the card to add is a set.

    for card_set in deck_set:
        # The next block checks the lenght of the card.
        if len(card_to_add_set) != len(card_set):
            print("Error! card is of wrong length")
            return False
        else:
            for card_set in deck_set:
                # The next block checks if the card has only one match with every other card.
                if len(card_to_add_set.intersection(card_set)) == 1:
                    deck.append(card)
                    return True
                elif len(card_to_add_set.intersection(card_set)) != 1:
                    print("Error! number of matches for new card is not one")
                    return False


# 4. Check if a deck is valid
def is_valid(deck):
    """
    This function checks if the deck is valid.
    It uses three other functions to better organize the code.
    """
    # The next block checks if every function returns the boolean True,
    # if so, the deck is valid.
    if check_string(deck) is True and check_card_size(deck) is True and \
            check_intersections(deck) is True:
        return True
    else:
        return False


def check_string(deck):
    """
    This function receives a deck (list of lists). It checks if every list 
    inside the outter is made exclusively by strings.
    """

    dict_type = dict() # Creates a dictionary to store all the possible classes of elements.
    type_counter = 0  # Counts how many different types of data are there in the deck.

    for card in deck:
        for symbol in card:
            if type(symbol) not in dict_type:  # If the type is not in the dictionary, creates it with the value 1.
                dict_type[type(symbol)] = 1
                type_counter += 1
            else: 
                dict_type[type(symbol)] += 1  # If the type is already in the dictionary, adds +1 to its value.
                type_counter += 1

    if type_counter == dict_type[str]:
        return True  # If only strings are found.
    else:
        return False  # If there is another data type in the list.


def check_card_size(deck):
    """
    This function receives a a deck (list of lists). It checks if every card 
    inside it has the same lenght.
    """
    dict_size = dict()  # Creates a dictionary to store every cards lenght.

    for card in deck:
        if tuple(card) not in dict_size:
            dict_size[tuple(card)] = len(card)  # Stores every cards lenght in the dictionary.

    set_of_lenght = {lenght for lenght in dict_size.values()}  # Creates a set with all the lenghts.

    # If there is only one element in the set, it means that every card has the same lenght.
    # Otherwise there would be more than one element in the set.

    if len(set_of_lenght) == 1:
        return True
    else:
        return False


def check_intersections(deck):
    """
    This function receives a deck (list of lists). It checks if every pair of
    cards has exactly one symbol in common.
    """

    # Creates a dictionary that stores every pair of cards as the keys
    # and the number of symbols in common as the value.
    dict_number_of_intersections = dict() 

    list_of_pairs = []
    for card in deck:
        # Makes a deepcopy of the deck in order to remove a card without
        # affecting the original deck.
        deck_without_card = copy.deepcopy(deck)  
        deck_without_card.remove(card)  
        # Removes a card in so there wont be a pair of the same card.
        for card_to_compare in deck_without_card:
            # Creates a pair of two cards and appends it to a list.
            # The list contains all the possible combinations of cards, 
            # except a pair where both cards are the same.
            pair_to_compare = tuple((tuple(card), tuple(card_to_compare)))
            list_of_pairs.append(pair_to_compare)

    for pair in list_of_pairs:
        # Store to the dictionary the pair as key and the number of 
        # common symbols as a value.
        dict_number_of_intersections[pair] = \
            len(cards_intersect(pair[0], pair[1]))

    # Creates a set of all the values.
    set_number_intersections = \
        {number for number in dict_number_of_intersections.values()}

    # If the set of values is {1}, it means that every card has 
    # exactly one match with every other card.
    if set_number_intersections == {1}:
        return True
    else:
        return False


# 5. Draw 2 cards at random
def draw_random_cards(deck):
    """
    This function receies a deck (list of lists) and returns two random cards 
    (lists) from the deck.
    """
    chosen_cards = random.sample(deck, 2)
    return chosen_cards


# 6. Print all symbols with counts
def print_symbols_counts(deck):
    """
    This function receives a deck (list of lists) and returns
    the number of symbols in the deck's cards.
    """
    # Creates a dictionary to store every symbol and how many times it appears.

    dict_number_symbols = dict()  

    # The next block modifies the dictionary to add every symbol as keys 
    # and how many times the symbol appears through the cards.
    for card in deck:
        for symbol in card:
            if symbol not in dict_number_symbols:
                dict_number_symbols[symbol] = 1
            else:
                dict_number_symbols[symbol] += 1

    # Prints every symbol and the number of apearances, one in each line.
    for key, value in dict_number_symbols.items():
        print("{} {}".format(key, value))


# 7. Interactive function for playing the game
def play_dobble(deck):
    """
    This function receives a deck (list of lists) and plays the game Dobble.
    This function uses the other functions created previously.
    """
    # Creates a deep copy of the deck to keep the original unaltered.
    deck_game = copy.deepcopy(deck)
    # Get option from user
    option = input(
        'Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n')

    # The next line calls the functions add_card, remove_card and 
    # print_symbols_count based on the users input.
    add_remove_count(deck, option)
    correct = 0  # Counts the correct guesses.
    wrong = 0  # Counts the wrong guesses.
    time_list = []  # Stores the time taken to guess every round.
    if option == "P":
        while len(deck_game) >= 2:
            print("Identify joint symbol:")
            cards = draw_random_cards(deck_game)  # Draws two cards.
            print(",".join(cards[0]))
            print(",".join(cards[1]))
            time_start = time.time()  # Starts counting the time.
            user_choice = input()  # Wait for users guess.
            answer = "".join(cards_intersect(cards[0], cards[1]))
            if user_choice == answer:  # Compare users guess with the answer.
                time_end = time.time()  # Stops counting the time.
                delta_time = round(time_end - time_start, 2)  # Calculates the times delta.
                print("Very nice! Found the correct card in {} sec."
                      .format(delta_time))
                time_list.append(delta_time)  # Appends the time to the list.
                correct += 1  # Adds +1 to the correct counter.
                # Removes both cards from the deck.
                remove_card(deck_game, cards[0])
                remove_card(deck_game, cards[1])
            else:  # If guess is wrong.
                time_end = time.time()  # Stops counting the time.
                print("Wrong!")
                wrong += 1  # Adds +1 to the wrong counter.
                # Removes both cards from the deck.
                remove_card(deck_game, cards[0])
                remove_card(deck_game, cards[1])

                delta_time = round(time_end - time_start, 2)  # Calculates the times delta.
                time_list.append(delta_time)  # Appends the time to the list.

        average_time = time_average(time_list)  # Variable with the average time.
        # Prints a message with the final score and the average time.
        print("Finished Game. Correct: {} Wrong: {} Average time: {} sec."
              .format(correct, wrong, average_time))


def time_average(lst):
    """
    This function receives a list of times taken to guess the correct answer
    from the previous function and returns the average, rounded to two decimal
    digits.
    """
    total_time = 0  # Starts a variable to store the total time.
    
    # Sums up the time.
    for time_taken in lst:
        total_time += time_taken
    
    # Returns the average time, rounded to two decimal digits.
    average = round(total_time / len(lst), 2)  
    return average


def add_remove_count(deck, option):
    """
    This function execute three different functions based
    on the users input on run_dobble function.
    """
    if option == "A":
        symbols = input()
        card = symbols.split(",")
        add_card(deck, card)
        return None

    if option == "R":
        symbols = input()
        card = symbols.split(",")
        remove_card(deck, card)
        return None

    if option == "C":
        print_symbols_counts(deck)


# 8. Bonus question: create deck as large as possible
def create_deck(symbols, k):
    deck = [symbols[
            :k]]  # This will create a deck with one card. Can you make it larger?
    return deck
    pass
