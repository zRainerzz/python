students=[
    {"name":"rainz","house":"west appartement","patronus":"outter"},
    {"name":"sys","house":"east","patronus":"easter"},
    {"name":"clair","house":"herbitic house","patronus":"ice"},
    {"name":"odiciz","house":"helland","patronus":None}
]
for student in students:
    print (student["name"], student["house"], student["patronus"] , sep=", " ,end=" / ")