# 4. Check if a deck is valid
def is_valid(deck):
    deck_set = {frozenset(card) for card in deck}

    
        
deck = [['lips', 'pencil', 'spider', 'exclamation point', 'scarecrow'],
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

print(is_valid(deck))