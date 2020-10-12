"""
    Kids Hack Labs
    Fall 2020 - Senior
    Week 02: Python Review
    Activity 3
"""
#Step 1: Random module import
import random

#Step 2: Function that prints a random number until the user
#        decides to quit
def randomizer():
    random.seed() #Seeding random engine
    finish = None
    while finish != "q":
        print(random.randint(1, 100))
        finish = input("Type \'q\' to exit, any other key to"+
                       " get another random number: ")

#step 3: function call
randomizer()

"""
    Obs.: Students are encouraged to investigate other
    functions in the random module that generate random
    numbers, and even functions that generate other number
    types such as floats.
"""
