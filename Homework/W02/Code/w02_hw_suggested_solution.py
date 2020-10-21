"""
    Kids Hack Labs
    Fall 2020 - Senior
    Week 02: Python Review
    Homework: Number guessing game
"""
#Step 1: random module import
import random

#Step 2: application main entry point
def main():
    #setup (steps 2.1 through 2.5)
    random.seed()
    tries = 5   #total tries granted
    guesses = 0 #total guesses made
    player_won = False
    target = random.randint(1, 63)

    #game loop(step 2.6 and sub-steps)
    while guesses < tries and not player_won:
        player_guess = int(input("Guess a number: "))
        guesses += 1

        if player_guess == target:
            player_won = True
        else:
            if player_guess < target:
                print("You guessed lower than the secret number.")
            else:
                print("you guessed higher than the secret number.")

    #Game end: Steps 2.7 and 2.8
    if player_won:
        print("You won the game in",guesses,"tries!")
    else:
        print("You lost the game... The secret number was",target)

if __name__ == "__main__":
    main()

"""
    Obs.: Students are encouraged to experiment with the code and try
    other techniques to generate the numbers or streamline the outputs
    to the user.
"""
