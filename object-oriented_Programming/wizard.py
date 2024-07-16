class Wizard:
    def __init__ (self,name):
        if not name:
            raise ValueError("Missing name. ")
        self.name=name


class Student(Wizard):
#this is called inheritance,class Student(Wizard): now the class Student inherit all the characteristics of the Wizard class.
    def __init__(self,house):
        super().__init__(name)
        #super is the reference to the super class of this class so if this class is student the super class, the parent class is wizard
        self.house=house




class Professor(Wizard):
    def __init__(self,subject):
        self.subject=subject
