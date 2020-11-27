# Template file for dobble
import copy
import random
import time


# 1. Intersect two cards
def cards_intersect(card1, card2):
    card1_set = set(card1)
    card2_set = set(card2)
    in_both = list(card1_set.intersection(card2_set))
    return in_both


# 2. Check if card is in deck and remove it
def remove_card(deck, card):
    deck_set = {frozenset(card) for card in deck}
    card_to_remove_set = frozenset(card)

    for card_list in deck:
        card_set = set(card_list)
        if len(card_set.intersection(card_to_remove_set)) == \
                len(card_to_remove_set):
            deck.remove(card_list)
            return True

    if card_to_remove_set not in deck_set:
        print("Error! card is not in the deck")
        return False


# print(remove_card([["dolphin","bomb","spider"],["eye","bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]],["spider","fire","lock"]))
# [["dolphin","bomb","spider"],["eye","bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]]

# 3. Check if new card matches and add it to the deck
def add_card(deck, card):
    deck_set = {frozenset(card) for card in deck}
    card_to_add_set = frozenset(card)

    for card_set in deck_set:
        if len(card_to_add_set) != len(card_set):
            print("Error! card is of wrong length")

    for card_set in deck_set:
        if len(card_to_add_set.intersection(card_set)) == 1:
            deck.append(card)
            return True
        elif len(card_to_add_set.intersection(card_set)) != 1:
            print("Error! number of matches for new card is not one")
            return False


# 4. Check if a deck is valid
def is_valid(deck):
    
    if check_string(deck) == True and check_card_size(deck)== True and\
         check_intersections(deck) == True:
        return True
    else:
        return False


def check_string(deck):
    dict_type = dict()
    symbol_counter = 0 # Counts how many symbols are in the deck
    
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
            pair_to_compare = tuple((tuple(card),tuple(card_to_compare)))
            list_of_pairs.append(pair_to_compare)
            deck_without_card = deck

    for pair in list_of_pairs:
        dict_number_of_intersections[pair] = \
            len(cards_intersect(pair[0],pair[1]))
    
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
                dict_number_symbols[symbol] +=1

    for key,value in dict_number_symbols.items():
        print("{} {}".format(key,value))


# 7. Interactive function for playing the game
def play_dobble(deck):
    option = input(
        'Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n')  # Get option from user
    

    # Fill code for each option
    pass


# 8. Bonus question: create deck as large as possible
def create_deck(symbols, k):
    deck = [symbols[
            :k]]  # This will create a deck with one card. Can you make it larger?
    return deck
    pass
