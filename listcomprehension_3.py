students=[
    {"name":"Hermoine", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
]

def is_gryffindor(s):
    return s["house"]=="Gryffindor"

gryffindors= filter(is_gryffindor,students)
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])


"""
similar in spirit to map, passing a function that is going to apply to each element in a sequence
but map returns 1 value for each element in a sequence, that's how it forced all the elements to uppercase.
but if we want conditionally include a student in my resulting gryffindor's list, i can use filter instead. this is a function that returns true or false. it tells me whether or not include or not include the current student from the final list.
and the question is being asked: do they live in gryffindor (is_gryffindor) or not by checking the dictionary's "house" key for that answer.
"""