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
    if card_to_remove_set in deck_set:
        deck_set.remove(card_to_remove_set)
        deck = [list(card_set) for card_set in deck_set]
        return True
    else:
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

# deck = [["dolphin","bomb","spider"],["eye","bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]]
# add_card(deck,["spider","eye","tree"])
# print(deck)



# 4. Check if a deck is valid
def is_valid(deck):
    # Fill code
    pass

# 5. Draw 2 cards at random
def draw_random_cards(deck):
    # Fill code
    pass


# 6. Print all symbols with counts
def print_symbols_counts(deck):
    # Fill code
    pass


# 7. Interactive function for playing the game
def play_dobble(deck):
    option = input('Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n') # Get option from user

    # Fill code for each option
    pass


# 8. Bonus question: create deck as large as possible
def create_deck(symbols, k):
    deck = [symbols[:k]]  # This will create a deck with one card. Can you make it larger?
    return deck
    pass





