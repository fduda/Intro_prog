import copy
deck = [["dolphin","bomb","spider"],["eye","bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]]

card = ["spider","fire","lock"]

def remove_card(deck, card):
    deck_set = {frozenset(card) for card in deck}
    
    card_to_remove_set = frozenset(card)
    if card_to_remove_set in deck_set:
        deck_set.remove(card_to_remove_set)
        deck = [list(card_set) for card_set in deck_set]
        return True
    else:
        return False

remove_card(deck,card)
# print(remove_card([["dolphin","bomb","spider"],["eye","bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]],["spider","fire","lock"]))
print(deck)