def _pick_coins(coins, p, pickers):

    # winner = ""

    # define picker
    picker = pickers[p]

    # choose how many coins to pick
    if coins==1:
        picked_coins = 1
    else:
        if coins%3==0:
            # lost, no matter what
            # print("{} lost here!".format(picker))
            # doesn't matter how many coins you pick
            picked_coins = 1
        elif coins%3==1:
            picked_coins = 4
        else:
            picked_coins = coins%3

    print(coins)
    print("{} picks {} coins".format(picker, picked_coins))
    print("----------------")

    # pick coins
    coins = coins - picked_coins
    # print("We are left with {} coins".format(coins))

    if coins==0:
        winner = picker
        print("{} Wins!".format(winner))
        return winner

    # switch picker (switches between 0 and 1)
    p = (p+1)%2
    picker = pickers[p]

    return _pick_coins(coins=coins, p=p, pickers=pickers)

    
    
# MAIN

n = 30
pickers = ["bob","ana"]

p = 0
picker= pickers[p]

winner = _pick_coins(coins=n, p=p, pickers = pickers)