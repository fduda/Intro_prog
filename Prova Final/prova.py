


from typing import List


def find_change_point(arr):
    # determine wgetger we search for max or min
    is_up = arr[0]< arr[1]
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) //2
        # if is_up and increasing or not and decreasing
        if (is_up and arr[mid-1] < arr[mid] < arr[mid+1]) or \
            (not is_up and arr[mid-1] > arr[mid] > arr[mid+1]):
            left = mid
        elif (is_up and arr[mid-1] > arr[mid] > arr[mid+1]) or \
            (not is_up and arr[mid-1] > arr[mid] > arr[mid+1]):
            right = mid
        else:
            return mid

def count_products(lst, target):
    if len(lst) == 0:
        if target == 1:
            return 1
        else:
            return 0
    return count_products(lst[1:], target) + \
        count_products(lst[1:], target/lst[0])

class EmpiricalDistribution:

    def __init__(self, lst = None):
        if lst == None:
            self.numbers = list()
        else:
            self.numbers = lst

    def add_number(self, number):
        self.numbers.append(number)
    
    def lower_than_or_equal(self, a):
        counter = 0
        for num in self.numbers:
            if num <= a:
                counter += 1
        return counter/len(self.numbers)
    
    def average(self):
        return sum(self.numbers) / len(self.numbers)

def shrink(x):
    sumList = []
    newSum = 0
    for i in range(0, len(x)):
        newSum += x[i]
        if i == len(x)-1 or x[i]*x[i+1]<0:
            sumList.append(newSum)
            newSum = 0
    return sumList

def subset(lst, k):
    if len(lst) == 1 or k == len(lst):
        return [lst]
    if k == 1:
        result = []
        for item in lst:
            result.append([item])
        return result
    
    sub1 = subset(lst[1:len(lst)],k)
    sub2 = subset(lst[1:len(lst)], k-1)
    for item in sub2:
        item.append(lst[0])
    return sub1 + sub2


def running_product():
    lst = []
    def product(x):
        lst.append(x)
        result = 1
        for item in lst:
            result *= item
        return result
    return product


class ChangeGiver:

    def __init__(self):
        self.cash{1:0, 5:0, 10:0}

    def add_coins(self, amount, coin):
        self.cash[coin] = self.cash[coin] + amount
    
    def print_sum(self):
        print(self.cash[1]+5*self.cash[5] + 10*self.cash[10])
    
    def calculate_change(self, change):
        currentChange, numCoins = change, {10:0, 5:0, 1:0}
        for coin in [10,5,1]:
            numCoins[coin] = min(currentChange//coin, self.cash[coin])
            currentChange = currentChange-numCoins[coin]*coin
        if currentChange == 0:
            for coin in [1,5,10]:
                self.cash[coin] = self.cash[coin]-numCoins[coin]
            return [numCoins[1], numCoins[5], numCoins[10]]
        else:
            return [0,0,0]