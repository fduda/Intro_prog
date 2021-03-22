def most_common(lst):
    dct = {}
    for i in lst:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1

    counter = 0
    for i in dct.values():
        if i>counter:
            counter = i
    for key, value in dct.items():
        if value == counter:
            return key



print(most_common(["alice", "bob", "alice", "carol", "carol", "alice"]))