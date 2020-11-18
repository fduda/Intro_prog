# Template file for dobble
import copy
import random
import time


# 1. Intersect two cards
def cards_intersect(card1, card2):
    final_card_set = set()
    for symbol1 in card1:
        for symbol2 in card2:
            if symbo1 == symbol2:
                final_card_set.add(symbol1)
    in_both = list(final_card_set)
    return in_both



# 2. Check if card is in deck and remove it
def remove_card(deck, card):
    # Fill code
    pass

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





