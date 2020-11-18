import copy
import random
import time

# # 2. Check if card is in deck and remove it
# def remove_card(deck, card):
#     deck_set = set()
#     for card in deck:
#         card = set(card)
#         deck_set.add(card)
#     return deck_set


# print(remove_card([["dolphin", "bomb","spider"],["eye", "bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]],None))
    
# [["dolphin", "bomb","spider"],["eye", "bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]]

def cards_intersect(card1, card2):
    card1_set = set(card1)
    card2_set = set(card2)
    in_both = list(card1_set.intersection(card2_set))
    return in_both

print(cards_intersect(["tortoise","dog","zebra"],["zebra","tortoise","cheese"]))

