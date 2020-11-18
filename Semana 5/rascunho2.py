import copy
import random
import time

# 2. Check if card is in deck and remove it
def remove_card(deck, card):
    deck_set = set()
    for card in deck:
        card = set(card)
        deck_set.add(card)
    return deck_set


print(remove_card([["dolphin", "bomb","spider"],["eye", "bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]],None))
    
# [["dolphin", "bomb","spider"],["eye", "bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]]
