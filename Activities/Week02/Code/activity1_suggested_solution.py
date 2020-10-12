"""
    Kids Hack Labs
    Fall 2020 - Senior
    Week 02: Python Review
    Activity 1
"""
#Step 1: Function that takes 2 arguments and displays greater
def greater(num_a, num_b):
    if num_a > num_b:
        print(num_a, "is greater than", num_b)
    else:
        print(num_b, "is greater than", num_a)

#step 2: Inputs from user (cast to integer) stored in variables
first = int(input("First number, please: "))
second = int(input("Second number, please: "))

#step 3: Calling function defined in step 1
greater(first, second)

"""
    Obs.: Inputs were cast to integers for comparison.
          The implementation does not account for
          equal numbers. The student is free to improve
          the code in that regard.
"""
