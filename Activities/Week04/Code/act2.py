"""
    Kids Hack Labs
    Fall 2020 - Senior
    Week 04: Introduction to Classes
    Activity 2
"""
#Suggested answer:
class Animal():
    def __init__(self, _type, _name, _legs, _sound):
        self.type = _type
        self.name = _name
        self.legs = int(_legs)
        self.sound = _sound

    def walk(self):
        for i in range(self.legs):
            print("step", end= " ")

    def make_sound(self):
        print(self.sound)

    def get_name(self):
        print("The "+self.type+"'s name is: "+self.name+".")

"""
    The following twelve lines should be input in the shell,
    once the current module is run. The names and data in the
    animals are simply suggestions, and serve to test the
    class's functions under different initial parameters

    puppy = Animal("dog", "Hacky", 4, "woof!")
    puppy.walk()
    puppy.make_sound()
    puppy.get_name()

    kitty = Animal("cat", "Nimbus", 4, "meow!")
    kitty.walk()
    kitty.make_sound()
    kitty.get_name()

    flappy = Animal("duck", "Chamille", 2, "Quack!")
    flappy.walk()
    flappy.make_sound()
    flappy.get_name()
"""
