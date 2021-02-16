class Parliament:

    def __init__(self, dct = None):
        if dct != None:
            self.dct = dct
        else:
            self.dct = {}
            


    def insert(self, party, mandates):
        total_mandates = 0
        for mandate in self.dct.values():
            total_mandates += mandate
        
        if total_mandates < 120-mandates:
            self.dct[party] = mandate
        else:
            print("the parliament is full")
    
    def unite(self, party1, party2):
        if party1 in self.dct and party2 in self.dct:
            mandate_unified_party = self.dct[party1] + self.dct[party2]
            name_unified_party = str(party1) + "-" + str(party2)

            self.dct.pop(party1)
            self.dct.pop(party2)
            self.dct[name_unified_party] = mandate_unified_party

    def check_coalition(self, lst):
        return sum([self.dct[key] for key in lst if key in self.dct]) >= 61


parties = {"pirates" : 13, "moomins" : 17, "ninja-turtles" : 28, "avengers" : 6, "power" : 7}

P = Parliament(parties)

P.insert("rangers", 8)
