#class is like a blueprint for pieces of data (objects) 
#a class is like a mold that you can define and give a name when you use that mold or use that blueprint you get types of data that are designed as you want.
#in short, classes allow you to invent your own data types in Python and give them a name and this is a primary feature of object oriented programming to be able to create your own objects this way and in case of python in classes. even give them some custom names.
class Student:
    ...
def main():
    student=get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student=Student()
    name=input("Name: ").capitalize()
    house=input("House: ").capitalize()
    return student

if __name__ == "__main__":
    main()
