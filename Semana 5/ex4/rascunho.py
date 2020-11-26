import copy
import  random


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
    


small_deck = [['dolphin', 'bomb', 'spider'], ['eye', 'bomb', 'fire'],
['spider', 'fire', 'lock'], ['bomb', 'lock', 'tree']]

big_deck = [['lips', 'pencil', 'spider', 'exclamation point', 'scarecrow'],
 ['scarecrow', 'maple leaf', 'scissors', 'snowflake', 'dog'],
 ['pencil', 'maple leaf', 'apple', 'stop', 'tree'],
 ['lips', 'maple leaf', 'iglu', 'eye', 'tortoise'],
 ['pencil', 'scissors', 'iglu', 'dolphin', 'bomb'],
 ['scarecrow', 'tree', 'tortoise', 'dolphin', 'zebra'],
 ['scarecrow', 'stop', 'iglu', 'sun', 'snowman'],
 ['spider', 'scissors', 'tree', 'eye', 'sun'],
 ['pencil', 'dog', 'eye', 'zebra', 'snowman'],
 ['scarecrow', 'apple', 'eye', 'bomb', 'moon'],
 ['lips', 'dog', 'apple', 'dolphin', 'sun'],
 ['exclamation point', 'maple leaf', 'bomb', 'zebra', 'sun'],
 ['spider', 'maple leaf', 'dolphin', 'snowman', 'moon'],
 ['exclamation point', 'scissors', 'apple', 'tortoise', 'snowman'],
 ['lips', 'scissors', 'stop', 'zebra', 'moon'],
 ['spider', 'dog', 'stop', 'tortoise', 'bomb'],
 ['lips', 'snowflake', 'tree', 'bomb', 'snowman'],
 ['exclamation point', 'snowflake', 'stop', 'eye', 'dolphin'],
 ['exclamation point', 'dog', 'tree', 'iglu', 'moon'],
 ['pencil', 'snowflake', 'tortoise', 'sun', 'moon']]

print(print_symbols_counts([['dolphin', 'bomb', 'spider'], ['scissors', 'spider', 'exclamation point']]))