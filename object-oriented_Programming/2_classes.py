#class is like a blueprint for pieces of data (objects) 
#a class is like a mold that you can define and give a name when you use that mold or use that blueprint you get types of data that are designed as you want.
#in short, classes allow you to invent your own data types in Python and give them a name and this is a primary feature of object oriented programming to be able to create your own objects this way and in case of python in classes. even give them some custom names.
class Student:
    def __init__ (self,first,middle, last , house,):
        if not first:
            raise ValueError("Invalid name, No first name? ")
        if not last:
            raise ValueError("Invalid Name, No last name? ")
        #init is used to initialize the contents of an object
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house.")
        self.first=first
        self.middle=middle
        self.last=last
        self.house=house
def main():
    student=get_student()
    if not student.middle:
        print(f"{student.first} {student.last} from {student.house}")
    else:
        print(f"{student.first} {student.middle} {student.last} from {student.house}")


def get_student():
    first=input("First Name: ").capitalize()
    middle=input("Middle Name (optional): ").capitalize()
    last=input("Last Name: ").capitalize()
    house=input("House: ").capitalize()
    return Student(first, middle, last, house)

if __name__ == "__main__":
    main()
