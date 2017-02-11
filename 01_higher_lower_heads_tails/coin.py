#!/usr/bin/python3

__author__ = 'doggra'

import time
import random

def main():

    choice = None
    correct_choices = {
        "H": "heads",
        "T": "tails",
    }

    print("Welcome to heads or tails!")

    while not choice:
        choice = input("Please choose (H)eads or (T)ails ").upper()

        if choice in correct_choices.keys():

            # Role play
            print("You pick {0}!".format(correct_choices[choice]))
            print("You toss a coin...")
            time.sleep(0.5)
            print("Coin rotates...")
            time.sleep(0.5)
            print("Coin rotates...")
            time.sleep(1)

            fate = random.randint(0,10)
            if (1 <= fate <= 5):
                wins = "H"
            elif (6 <= fate <= 10):
                wins = "T"
            elif fate == 0:
                print("Coin stood on the edge! Nobody wins!")
                quit(0)

            if choice == wins:
                winner = "Human"
            else:
                winner = "Computer"

            print("{0}! {1} wins!".format(correct_choices[wins].title(), winner.upper()))

        else:
            print("Wrong answer. Try again.")
            choice = None

if __name__ == '__main__':
    main()
