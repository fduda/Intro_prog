# Template file for dobble
import copy
import random
import time


# 1. Intersect two cards
from typing import List, Any


def cards_intersect(card1, card2):
    card1_set = set(card1)
    card2_set = set(card2)
    in_both = list(card1_set.intersection(card2_set))
    return in_both


# 2. Check if card is in deck and remove it
def remove_card(deck, card):

    final_deck = []
    for i in range(len(deck)):
        deck[i] = frozenset(deck[i])
    deck_set = set(deck)

    card_set = set(card)
    if card_set in deck_set:
        deck_set.remove(card_set)
        
    elif card_set not in deck_set:
        print("Error! card is not in the deck")
        return False

    
    for card_set in deck_set:
        card_list = list(card_set)
        final_deck.append(card_list)
    
    return True



# 3. Check if new card matches and add it to the deck
def add_card(deck, card):
    # Fill code
    pass


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





