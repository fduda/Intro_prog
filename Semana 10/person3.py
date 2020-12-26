from car import Car


class Person:

    def __init__(self, age, name, id):
        self.id = id
        self.name = name
        self.age = age
        self.car = Car

    
    def celebrate_birthday(self):
        self.age += 1
    
    def change_name(self, new_name):
        self.name = new_name

    def drive(self, km):
        self.car.drive(km)

    
person1 = Person(42,"Rob", 222222)
person1.celebrate_birthday()
print(person1.age)
person1.drive(4)

 