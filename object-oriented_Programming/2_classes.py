#class is like a blueprint for pieces of data (objects) 
#a class is like a mold that you can define and give a name when you use that mold or use that blueprint you get types of data that are designed as you want.
#in short, classes allow you to invent your own data types in Python and give them a name and this is a primary feature of object oriented programming to be able to create your own objects this way and in case of python in classes. even give them some custom names.
class Student:
    def __init__ (self,first,middle, last , house, patronus):
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
        self.patronus=patronus
    def charm(self):
        #__init__ and __str__ are special methods (functions in classes are called methods) and now we are creating our own method.
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russle terrier":
                return "🐶"
            case _:
                return "No patronus = No charm :)"
def main():
    student=get_student()
    print("expecto patronum!")
    if not student.middle:
        print(f"{student.first} {student.last} from {student.house} and patronus is: {student.patronus} charm: ", student.charm())
    else:
        print(f"{student.first} {student.middle} {student.last} from {student.house} and patronus is: {student.patronus} charm:", student.charm())


def get_student():
    first=input("First Name: ").capitalize()
    middle=input("Middle Name (optional): ").capitalize()
    last=input("Last Name: ").capitalize()
    house=input("House: ").capitalize()
    patronus=input("Patronus: ").capitalize()
    return Student(first, middle, last, house, patronus)

if __name__ == "__main__":
    main()
