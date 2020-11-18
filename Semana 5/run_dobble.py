# Code for running the dobble functions
# All function calls should work after you implement them correctly
from ex4 import *

small_deck = [['dolphin', 'bomb', 'spider'], ['eye', 'bomb', 'fire'],
['spider', 'fire', 'lock'], ['bomb', 'lock', 'tree']]

add_card(small_deck, ['spider', 'eye', 'tree'])
remove_card(small_deck, ['dolphin', 'bomb', 'spider'])
print(draw_random_cards(small_deck))

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

print_symbols_counts(big_deck)
is_valid(big_deck)
play_dobble(big_deck)  # play game


# Create a new deck
symbols = ['stop', 'exclamation point', 'maple leaf', 'bomb', 'moon', 'heart',
 'sun', 'iglu', 'pencil', 'scarecrow', 'spider', 'snowflake', 'dolphin', 'tortoise',
 'apple', 'treble clef', 'scissors', 'dog', 'zebra', 'tree', 'eye', 'lips', 'snowman']
new_deck = create_deck(symbols, 5)

