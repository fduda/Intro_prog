import copy


def remove_card(deck, card):
    deck_set = {frozenset(card) for card in deck}
    card_to_remove_set = frozenset(card)

    for card_list in deck:
        card_set = set(card_list)
        if len(card_set.intersection(card_to_remove_set)) == \
                len(card_to_remove_set):
            deck.remove(card_list)
            return True
        else:
            print("Error! card is not in the deck")
            return False


deck = [["dolphin", "bomb", "spider"], ["eye", "bomb", "fire"],
        ["spider", "fire", "lock"], ["bomb", "lock", "tree"]]
# card = ["spider","fire","lock"]

remove_card(deck, ["spider", "fire", "lock"])
print(deck)

# def set_zero(lst,i):
#     lst[i] = 0

# my_list = [1,2,3]
# set_zero(my_list,1)
# print(my_list)


# print(deck)
# print(remove_card([["dolphin","bomb","spider"],["eye","bomb","fire"],["spider","fire","lock"],["bomb","lock","tree"]],["spider","fire","lock"]))
