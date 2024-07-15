class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name.")
        self.name=name
        self.house=house




class Professor:
    def __init__(self,name,subject):
        if not name:
            raise ValueError("Missing name.")
        self.name=name
        self.subject=subject
