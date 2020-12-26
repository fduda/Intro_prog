class Person:
    
    def init_person(age,name,id):
        person = Person()
        person.id = id
        person.name = name
        person.age = age
        return person
    
    def celebrate_birthday(self):
        self.age += 1

    def change_name(self, new_name):
        self.name = new_name
    

person1 = Person.init_person(42,"Rob", 222222)
person1.celebrate_birthday()
print(person1.age)

person1.change_name("Jesus")
print(person1.name)