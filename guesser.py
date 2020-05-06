###### The Guessing Game ######

# Program asks user to guess which number the computer is "Thinking" of.
# Then the user enters a number for the computer to "guess."
# Written by: Jerry Sypkens

import random
import os

### generates secret_number ###

user_name = "User"
secret_number = random.randint(0, 100)
greatest_num = 10 ** 10000 # program works up to 1- with 10000 zeros after it.

### Gets user name ###

def get_name():
    user_name = input("What is your name?: ")
    print("")
    return user_name

### User gueses number ###

def guess_number():
    print("")
    user_name = get_name()
    print("")
    # print(user_name + " please guess a number. I am thinking of a number between 0 and 100: ")
    user_guess = int(input(user_name + " please guess a number. I am thinking of a number between 0 and 100: "))
    print("")

    while user_guess != secret_number:
        for guesses_taken in range(1, 7):
            if user_guess > secret_number and user_guess <= 100 and user_guess >= 0:
                print(user_name + " guess " + str(user_guess) + " is too high, try again: ")
                print("")
                user_guess = int(input())
                print("")
            elif user_guess < secret_number and user_guess <= 100 and user_guess >= 0:
                print(user_name + " guess " + str(user_guess) + " is too low, try again: ")
                print("")
                user_guess = int(input())
                print("")
            elif user_guess == secret_number:
                break
            else:
                print("Invalid entry, try again...")
                user_guess = int(input())


        if secret_number == user_guess:
            print("Wow!!! You are a good guesser " + user_name + ". You chose " + str(user_guess) + " and I guessed " + str(secret_number) + "!")
        else:
            print("Enough guesses! I guessed the number " + str(secret_number))
        break
    menu()

### Computer guesses your number ###

def computer_guess():
    computer_num = random.randint(0, greatest_num) # guesses random number
    print("")
    print("Did you know that your computer is much better at guessing than humans???")
    print("")
    print("Here is an example...")
    print("")
    # print(user_name + " please enter any number for the computer to guess:")
    try:
        user_num = int(input(user_name + " please enter any number for the computer to guess: "))
    except ValueError:
        print("")
        print("Invalid entry! Please try again...")
        computer_guess()

    while user_num > greatest_num or user_num < 0:
        print("")
        user_num = int(input("Invalid entry. Please enter another number for the computer to guess: "))

    counter = 0
    high_num = greatest_num
    low_num = 0
    print("")

    while computer_num != user_num:
        for guesses_taken in range(1, greatest_num):
            counter += 1
            if computer_num > user_num:
                print("Guess # " + str(counter) + " was: " + str(computer_num))
                high_num = computer_num
                computer_num = random.randint(low_num, high_num)
            elif computer_num < user_num:
                print("Guess # " + str(counter) + " was: " + str(computer_num))
                low_num = computer_num
                computer_num = random.randint(low_num, high_num)
            elif computer_num == user_num:
                break
    print("Guess # " + str(counter) + " was: " + str(computer_num))
    print("")
    print("It took the computer " + str(counter) + " guesses to find your number of: " + str(computer_num))
    menu()

### menu function ###
def menu():
    print("")
    print("")
    hash_tag = ["#" for i in range(1, 8)]
    for a in range(1, 6):
        print(hash_tag)
    print("")
    print("###### The Guessing Game ######")
    print("")
    print("~ Please select an option: ~")
    print("(1) Guess A Number Game")
    print("(2) Computer Guesser")
    print("(3) Exit")
    print("")
    for a in range(1, 6):
        print(hash_tag)
    print("")
    # print("Enter number from selection: ")
    menu_input = input("Enter number from selection: ")

    if menu_input == "1" or menu_input == "2" or menu_input == "3":
        if menu_input == "1":
            guess_number()
        elif menu_input == "2":
            computer_guess()
        elif menu_input == "3":
            for i in range(1, 10000):
                for i in range(1, 10):
                    print("#")
                for i in range(1, 20):
                    print("Thank you! Have a nice day.")
                for i in range(1, 10):
                    print("#")
            os.system("clear")
            quit()
    else:
        print("Invalid selection. Try Again!")
        print("")
        print("")
        print("")
        menu()

# os.system("cat guesser.py") # Shows code before running program
print("")
### Menu ###
menu()
