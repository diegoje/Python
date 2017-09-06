#!/usr/bin/env python3
"""this is my first program
"""
import random


def main():
    random_number = random.randint(1, 10)
    found = False
    while not found:
        userGuess = int(input("Your guess: "))
        if userGuess == random_number:
            print("You got it!")
            found = True
            restart()
        elif userGuess > random_number:
            print("Guess lower!")
        else:
            print("Guess higher!")


def restart():
    play_again = str(input("Thanks for playing. Play again? (Y/N)"))
    if play_again == "Y":
        main()
    else:
        print("Bye bye!")


if __name__ == "__main__":
    main()
