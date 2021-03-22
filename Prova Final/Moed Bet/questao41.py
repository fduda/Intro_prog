class Multidict:

    def __init__(self, dct = None):
        if dct == None:
            self.dct = dct()
        else:
            self.dct = dct

    def add_to_key(self, key, value):
        self.dct[key] = value

    def has_value(self,key,value):
        if self.dct[key] == value:
            return True
        else:
            return False
dct = dict()
d = Multidict(dct)
d.add_to_key("f", 1)
d.add_to_key("g", 2)
d.add_to_key("f", 3)
print(d.has_value("f", 1))
print(d.has_value("g", 3))
print(d.has_value("f", 3))
