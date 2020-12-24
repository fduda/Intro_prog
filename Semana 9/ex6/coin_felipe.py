def coin_pick(n, p):

    players = ["first_player", "second_player"]  # Players in the game.
    picker = players[p]

    if n == 1:
        picked_coins = 1
    else:
        if n%3 == 0:
            picked_coins = 1
        elif n%3 == 1:
            picked_coins = 4
        else:
            picked_coins = n%3
        
        
    print(n)
    print("{} picks {} coins".format(picker,picked_coins))
    print("------------------------")

    n = n -picked_coins

    if n == 0:
        winner = picker
        print("{} Wins!".format(winner))
        return winner

    p = (p+1)%2  # Alternates between the players.
    picker = players[p]

    return coin_pick(n, p)

p=0
coin_pick(30, p)