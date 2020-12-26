
# %%
def choose_branches(n, picker):  # smart choices

    if picker == "first_player":
        if n == 1:
            p1 = 1
            p2 = 2
        else:
            if n % 3 == 0:
                p1 = n+1
                p2 = n+1
            # elif n % 3 == 1:
            #     p1 = 4
            #     p2 = n+1
            else:
                r = n % 3
                p1 = r
                p2 = r + 3
                if p2>4:
                    p2=n+1
        _left = n - p1
        _center = -1
        _right = n - p2

        return _left, _center, _right

    if picker == "second_player":
        _left = n - 1
        _center = n - 2
        _right = n - 4
        return _left, _center, _right


# %%
def dfs(n, players, counter=0, p=0, verbose=False):
    
    picker = players[p]

    if verbose:
        print("\n")    
        print("Branch: {}".format(n))
        print("----------------")    

    if n<0:
        return counter
    elif n==0:
        counter += 1
        return counter
    else:
        _left, _center, _right = choose_branches(n, picker)
        if verbose:
            print("Branching: ({},{},{})".format(_left, _center, _right))
    

    p = (p+1) % 2  # Alternates between the players.
    picker = players[p]

    counter = dfs(_left, players=players, counter=counter, p=p)
    counter = dfs(_center, players=players, counter=counter, p=p)
    counter = dfs(_right, players=players, counter=counter, p=p)
    
    return counter

# %%
def make_game(players, n_0):

    print("## NEW GAME")
    print("Players: ", players)
    print("Starting Pile of Coins: ", n_0)
    print("\n")

    if n_0 % 3 == 0:
        print("Calculating Losses")
        print("==================")
        winner = players[1]
        players = players[::-1]
    else:
        print("Calculating Wins")
        print("==================")
        winner = players[0]

    possibilities = dfs(n_0, players=players, counter=0, p=0)
    
    return winner, possibilities


# %%
%%time

# define list of players in order
players = ["first_player", "second_player"]

# running game
winner, possiblities = make_game(players, 3)
print("Winner: {} ({} possibilities)".format(winner, possiblities))

# %%
