def metro(lst):
    passengers_boarding = 0
    passengers_getting_off = 0

    for station in lst:
        passengers_boarding += station[0]
        passengers_getting_off += station[1]

    delta_passengers = passengers_getting_off - passengers_boarding
    if delta_passengers == 0:
        return True
    return False

lst1 = [[3,1],[4,1],[0,2],[1,3]]
lst2 = [[3,1],[4,1],[0,2],[1,4]]

print(metro(lst2))