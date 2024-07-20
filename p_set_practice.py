students=[
    {"name":"Hermoine", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
    {"Name":"Padma", "house":"Ravenclaw"},
]
houses = set()
#i called a function called set that's going to return to me some object in Python that represents this notion of a set wherein duplicates are automatically eleminated.
for student in students:
    houses.add(student["house"])
for house in sorted(houses):
    print (house)