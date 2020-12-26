ID_KEY = "id_of_person"

def init_person(age,name,id):
    person = {}
    person["age"] = age
    person["name"] = name
    person[ID_KEY] = id
    return person

def get_id_from_person(person):
    return person[ID_KEY]

def celebrate_birthday(person):
    person["age"] += 1

