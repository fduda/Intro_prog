# def remove_card(deck, card):
#     deck_set = {frozenset(card) for card in deck}
#     card_to_remove_set = set(card)

#     if card_to_remove_set in deck_set:

#         deck.remove(card_to_remove_set)

# 2. Check if card is in deck and remove it


def remove_card(deck, card):
    deck_set = {frozenset(card) for card in deck}
    card_to_remove_set = frozenset(card)

    for card_list in deck:
        card_set = set(card_list)
        if len(card_set.union(card_to_remove_set)) == \
                len(card_to_remove_set):
            deck.remove(card_list)
            return True

    if card_to_remove_set not in deck_set:
        print("Error! card is not in the deck!")
        return False
        
        




small_deck = [['dolphin', 'bomb', 'spider'], ['eye', 'bomb', 'fire'],
['spider', 'fire', 'lock'], ['bomb', 'lock', 'tree']]

remove_card(small_deck,['dolphin','spider','bomb'])
print(small_deck)