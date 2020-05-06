###### The Guessing Game ######

# Program asks user to guess which number the computer is "Thinking" of.
# Written by: Jerry Sypkens

import random

user_name = ""
secret_number = random.randint(0, 100)

def guess_number():
    user_guess_str = input()
    user_guess = int(user_guess_str)
    i = 0

    while user_guess != secret_number:
        while i < 7:
            if user_guess > secret_number and user_guess <= 100 and user_guess >= 0:
                print(user_name + " guess is too high, try again: ")
                user_guess_str = input()
                user_guess = int(user_guess_str)
            elif user_guess < secret_number and user_guess <= 100 and user_guess >= 0:
                print(user_name + " guess is too low, try again: ")
                user_guess_str = input()
                user_guess = int(user_guess_str)
            elif user_guess == secret_number:
                break
            else:
                print("Invalid entry, try again...")
                user_guess_str = input()
                user_guess = int(user_guess_str)
                i += 1
        if secret_number == user_guess:
            print("Wow!!! You are a good guesser " + user_name + ". You chose " + str(user_guess) + " and I guessed " + str(secret_number) + "!")
        else:
            print("Enough guesses! I guessed the number " + str(secret_number))


def get_name(user_name):
    print("What is your name?: ")
    user_name = input()
    print(user_name + " please guess a number. I am thinking of a number between 0 and 100: ")
    return user_name

user_name = get_name(user_name)
guess_number()
