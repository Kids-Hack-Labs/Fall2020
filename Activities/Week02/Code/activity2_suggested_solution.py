"""
    Kids Hack Labs
    Fall 2020 - Senior
    Week 02: Python Review
    Activity 2
"""
#Step 1: Function that repeats text
def repeater(txt):
    for i in range(5):
        print(txt)

#ALTERNATIVE IMPLEMENTATION:
def alt_repeater(txt):
    txt += "\n" #Adds a line break to the end of the text
    print(txt*5)

#Step 2: User input
text = input("What text do you wish to repeat? ")

#Step 3: Function call
repeater(text)
print("Calling alt_repeater(), for comparison")
alt_repeater(text)

"""
    The alt_repeater function below works in a similar,
    but different, way. It adds a line break character
    to the text (\n) and then uses a multiplication to
    print the text repeatedly. Students are encouraged
    to explore other available methods in the Python
    language as well
"""
