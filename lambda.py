people = [
    {"name": "Harry", "house": "Gryiffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

people.sort(key=lambda person: ["name"])
print(people)