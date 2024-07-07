def main():
    student=get_student()
    if student["name"]=="padma" or student["name"]=="Padma":
        student["house"]="ravenclaw"
    print(f"{student['name']} from {student['house']}").capitalize()


def get_student():
    name=input("Name: ")
    house=input("House: ")
    return {"name":name, "house":house}


if __name__ == "__main__":
    main()
