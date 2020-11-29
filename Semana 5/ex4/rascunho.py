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

    # The next two lines convert the card and the deck from lists to sets.
    deck_set = {frozenset(card) for card in deck} # Set of frozensets.
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
    deck_set = {frozenset(card) for card in deck} 
    card_to_add_set = frozenset(card)

    for card_set in deck_set:
        if len(card_to_add_set) != len(card_set):
            print("Error! card is of wrong length")
            return False
        else:
            for card_set in deck_set:
                if len(card_to_add_set.intersection(card_set)) == 1:
                    deck.append(card)
                    return True
                elif len(card_to_add_set.intersection(card_set)) != 1:
                    print("Error! number of matches for new card is not one")
                    return False


# 4. Check if a deck is valid
def is_valid(deck):
    if check_string(deck) is True and check_card_size(deck) is True and \
            check_intersections(deck) is True:
        return True
    else:
        return False


def check_string(deck):
    dict_type = dict()
    symbol_counter = 0  # Counts how many symbols are in the deck

    for card in deck:
        for symbol in card:
            if type(symbol) not in dict_type:
                dict_type[type(symbol)] = 1
                symbol_counter += 1
            else:
                dict_type[type(symbol)] += 1
                symbol_counter += 1

    if symbol_counter == dict_type[str]:
        return True
    else:
        return False


def check_card_size(deck):
    dict_size = dict()

    for card in deck:
        if tuple(card) not in dict_size:
            dict_size[tuple(card)] = len(card)

    set_of_lenght = {lenght for lenght in dict_size.values()}

    if len(set_of_lenght) == 1:
        return True
    else:
        return False


def check_intersections(deck):
    dict_number_of_intersections = dict()

    list_of_pairs = []
    for card in deck:
        deck_without_card = copy.deepcopy(deck)
        deck_without_card.remove(card)
        for card_to_compare in deck_without_card:
            pair_to_compare = tuple((tuple(card), tuple(card_to_compare)))
            list_of_pairs.append(pair_to_compare)

    for pair in list_of_pairs:
        dict_number_of_intersections[pair] = \
            len(cards_intersect(pair[0], pair[1]))

    set_number_intersections = \
        {number for number in dict_number_of_intersections.values()}

    if set_number_intersections == {1}:
        return True
    else:
        return False


# 5. Draw 2 cards at random
def draw_random_cards(deck):
    chosen_cards = random.sample(deck, 2)
    return chosen_cards


# 6. Print all symbols with counts
def print_symbols_counts(deck):
    dict_number_symbols = dict()

    for card in deck:
        for symbol in card:
            if symbol not in dict_number_symbols:
                dict_number_symbols[symbol] = 1
            else:
                dict_number_symbols[symbol] += 1

    for key, value in dict_number_symbols.items():
        print("{} {}".format(key, value))


# 7. Interactive function for playing the game
def play_dobble(deck):
    deck_game = copy.deepcopy(deck)
    # Get option from user
    option = input(
        'Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n')
    add_remove_count(deck, option)
    correct = 0
    wrong = 0
    time_list = []
    if option == "P":
        while len(deck_game) >= 2:
            print("Identify joint symbol:")
            cards = draw_random_cards(deck_game)
            print(",".join(cards[0]))
            print(",".join(cards[1]))
            time_start = time.time()
            user_choice = input()
            answer = "".join(cards_intersect(cards[0], cards[1]))
            if user_choice == answer:
                time_end = time.time()
                delta_time = round(time_end - time_start, 2)
                print("Very nice! Found the correct card in {} sec."
                      .format(delta_time))
                time_list.append(delta_time)
                correct += 1
                remove_card(deck_game, cards[0])
                remove_card(deck_game, cards[1])
            else:
                print("Wrong!")
                wrong += 1
                remove_card(deck_game, cards[0])
                remove_card(deck_game, cards[1])
                time_list.append(0)

        average_time = time_average(time_list)
        print("Finished Game. Correct: {} Wrong: {} Average time: {} sec."
              .format(correct, wrong, average_time))


def time_average(lst):
    total_time = 0
    for time_taken in lst:
        total_time += time_taken

    average = round(total_time / len(lst), 2)
    return average


def add_remove_count(deck, option):
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


big_deck = [['lips', 'pencil', 'spider', 'exclamation point', 'scarecrow'],
 ['scarecrow', 'maple leaf', 'scissors', 'snowflake', 'dog'],
 ['pencil', 'maple leaf', 'apple', 'stop', 'tree'],
 ['lips', 'maple leaf', 'iglu', 'eye', 'tortoise'],
 ['pencil', 'scissors', 'iglu', 'dolphin', 'bomb'],
 ['scarecrow', 'tree', 'tortoise', 'dolphin', 'zebra'],
 ['scarecrow', 'stop', 'iglu', 'sun', 'snowman'],
 ['spider', 'scissors', 'tree', 'eye', 'sun'],
 ['pencil', 'dog', 'eye', 'zebra', 'snowman'],
 ['scarecrow', 'apple', 'eye', 'bomb', 'moon'],
 ['lips', 'dog', 'apple', 'dolphin', 'sun'],
 ['exclamation point', 'maple leaf', 'bomb', 'zebra', 'sun'],
 ['spider', 'maple leaf', 'dolphin', 'snowman', 'moon'],
 ['exclamation point', 'scissors', 'apple', 'tortoise', 'snowman'],
 ['lips', 'scissors', 'stop', 'zebra', 'moon'],
 ['spider', 'dog', 'stop', 'tortoise', 'bomb'],
 ['lips', 'snowflake', 'tree', 'bomb', 'snowman'],
 ['exclamation point', 'snowflake', 'stop', 'eye', 'dolphin'],
 ['exclamation point', 'dog', 'tree', 'iglu', 'moon'],
 ['pencil', 'snowflake', 'tortoise', 'sun', 'moon']]

play_dobble(big_deck)
