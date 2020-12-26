def choose_branches(n, picker):  # smart choices

    if picker == "first_player":
        if n == 1:
            p1 = 1
            p2 = -1
        else:
            if n % 3 == 0:
                p1 = -1
                p2 = -1
            elif n % 3 == 1:
                p1 = 4
                p2 = 1
            else:
                r = n % 3
                p1 = r
                p2 = r + 3
        _left = n - p1
        _center = -1
        _right = n - p2

        return _left, _center, _right

    if picker == "second_player":
        _left = n - 1
        _center = n - 2
        _right = n - 4
        return _left, _center, _right


def dfs(n, counter=0, p=0):


    players = ["first_player", "second_player"]  # Players in the game.
    picker = players[p]

    _left, _center, _right = choose_branches(n, picker)

     
    if _left == 2 or _left == 4 or _left == 1:
        counter += 1
        return counter


    print(n)
    print("----------------")
    

    p = (p+1) % 2  # Alternates between the players.
    picker = players[p]

    if _left > 0:
        dfs(_left, counter=counter, p=p)
    if _center > 0:
        dfs(_center, counter=counter, p=p)
    if _right > 0:
        dfs(_right, counter=counter, p=p)
    
    return None


number = dfs(10, counter=0, p=0)
print(number)
