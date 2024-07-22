students=["Hermoine","Harry","Ron"]

for i, student in enumerate(students):
    print(i,+1, students)

    """
    so with enumerate you won't need an index into the list with bracket i notation,
    you dont need to call range or len 
    because enumerate takes a sequence of values like these students and allows me to get back the current index 0 1 2 and the current value Hermoine Harry Ron
    """