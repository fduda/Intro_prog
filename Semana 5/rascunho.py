import copy
import random
import time

# 2. Check if card is in deck and remove it
# def remove_card(deck, card):

#     final_deck = []
#     for i in range(len(deck)):
#         deck[i] = frozenset(deck[i])
#     deck_set = set(deck)

#     card_set = set(card)
#     if card_set in deck_set:
#         deck_set.remove(card_set)
        
#     elif card_set not in deck_set:
#         print("Error! card is not in the deck")
#         return False

    
#     for card_set in deck_set:
#         card_list = list(card_set)
#         final_deck.append(card_list)
    
#     return True

# print(remove_card([["dolphin", "bomb","spider"],["eye", "bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]],["spider","fire","lock",]))
    
# [["dolphin", "bomb","spider"],["eye", "bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]]
import math

# def weird(n):
#     return [x for x in range(2,round(math.sqrt(n))) if n%(x*x) == 0]

# print(weird(9))

lst = [x for x in range(2,round(math.sqrt(4))) if 4%(x*x)==0]

print(round(math.sqrt(10)))
