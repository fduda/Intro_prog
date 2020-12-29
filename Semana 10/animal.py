# class Animal:
#     LEGS = 4
#     def __init__(self, kg):
#         self.__kg = kg
    
#     def eat(self, kg):
#         self.__kg += kg
    
#     def poop(self, kg):
#         if kg > self.__kg:
#             print("eat first")
#         else:
#             self.__kg -= kg

# cat = Animal(3)
# cat.poop(5)
# cat.eat(3)
# print(cat.__kg)

class Animal:
    LEGS = 4
    def __init__(self, kg):
        self.kg = kg
    def eat(self, kg):
        self.kg += kg
    def poop(self, kg):
        if kg > self.kg:
            print('eat first!')
        else:
            self.kg -= kg

# def f(lst):
#     if len(lst) == 1:
#         return lst
#     return [lst[len(lst)-1]] + f(lst[0:len(lst)-1])
# print(f([1,2,3,4,5,6]))

def f(num):
    if num == 1:
        return  str(num)
    return str(num)*num + f(num-1)

# print(f(4))

class Animal:
    LEGS = 4

dog = Animal()
bird = Animal()
bird.LEGS = 2
print(dog.LEGS, bird.LEGS)

