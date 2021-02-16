class EmpiricalDistribution:

    def __init__(self, lst = None):
        if lst == None:
            self.numbers = lst()
        else:
            self.numbers = lst

    def add_number(self, number):
        self.numbers.append(number)

    def lower_that_or_equal(self,a):
        counter = 0
        for number in self.numbers:
            if number <= a:
                counter += 1
        return counter/len(self.numbers)
    
    def average(self):
        total = sum(self.numbers))
        return total/len(self.numbers)