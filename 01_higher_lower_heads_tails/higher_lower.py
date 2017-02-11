#!/usr/bin/python3

import random

def main():

    choice = None
    correct_choices = ["H", "L", "E"]

    start_number = random.randint(1,1000)
    print("Computer selected number: {0}".format(start_number,))

    while not choice:
        choice = input("Next number going to be (H)igher, (L)ower or (E)qual? ").upper()
        if choice in correct_choices:
            end_number = random.randint(1,1000)
            if (choice == "H" and start_number < end_number) or (choice == "L" and start_number > end_number):
                print("Next number was {0}. You win!".format(end_number))
            elif choice == "E" and start_number == end_number:
                print("Wow! You are lucky, it's exacly the same ({0})".format(end_number,))
            else:
                print("Next number was {0}. You lose.".format(end_number,))
            break

        else:
            print("Wrong answer. Try again.")
            choice = None

if __name__ == '__main__':
    main()
