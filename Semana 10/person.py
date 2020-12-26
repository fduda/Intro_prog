class Person:
    pass

def init_person(age,name,id):
    person = Person()
    person.id = id
    person.name = name
    person.age = age
    return person

person = init_person(42,"Rob", 222222)

print(person.id)
print(type(person))
print(type("ola"))