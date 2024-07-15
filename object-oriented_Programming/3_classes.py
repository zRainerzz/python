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
        def __str__(self):
            return f"{self.last} {self.first} {self.middle} from {self.house}"
        #use it to print the message, instead of printing it from the main function. it will have the priority
        #__init__ and __str__ are special methods (functions in classes are called methods) and now we are creating our own method.
def main():
    student=get_student()
    print(student)


def get_student():
    first=input("First Name: ").capitalize()
    middle=input("Middle Name (optional): ").capitalize()
    last=input("Last Name: ").capitalize()
    house=input("House: ").capitalize()
    return Student(first, middle, last, house)

if __name__ == "__main__":
    main()
