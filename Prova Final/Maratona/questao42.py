class Histogram:

    def __init__(self):
        self.lst = []
        self.dct = {}

    def insert(self,numbers):
        for item in numbers:
            if item in self.dct:
                self.dct[item] += 1
            else:
                self.dct[item] = 1 

    def freq(self, a):
        if a in self.dct:
            return self.dct[a] / sum(self.dct.values())
        else:
            return 0

    def average(self):
        return sum([key*value for key,value in self.dct.items()]) / sum(self.dct.values())

