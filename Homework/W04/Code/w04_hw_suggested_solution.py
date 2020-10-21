"""
    Kids Hack Labs
    Fall 2020 - Senior
    Week 04: Application lifetime
    In-class activity 1
"""
#Suggested answer:

class Person():
    def __init__(self, _name, _age, _height, _weight):
        self.name = _name
        self.age = int(_age)
        self.height = float(_height)
        self.weight = float(_weight)

    def greet(self):
        print("Hi, my name is "+self.name)

    def get_age(self):
        print(self.name,"is",self.age,"years old")

    def drive_home(self):
        print(self.name, end = " ")
        if self.age < 16:
            print("cannot drive", end = " ")
        else:
            print("is driving", end=" ")
        print("home.")

    def get_bmi(self):
        print(self.name+"'s BMI is: ",self.weight/self.height**2)

"""
    The following lines of code serve as a suggestion to test
    the class's functions, and should be input in the shell.
    The student should attempt to create Person objects
    of their own:

    herc = Person("HErC", 35, 1.8, 78)
    herc.greet()
    herc.get_age()
    herc.drive_home()
    herc.get_bmi()
"""
