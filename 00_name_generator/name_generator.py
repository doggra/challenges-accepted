#!/usr/bin/python3

__author__ = "doggra"


import locale
from objects import Identity

def generate_names(count, gender):
    """ True generator """

    def new_identity_generator(gender):
        yield Identity(gender=gender)

    for i in range(int(count)):
        next(new_identity_generator(gender))

def main():

    # Number of names to generate
    try:
        count = input("Choose number of names (1-1000) (default: 1) ")
        count = int(count)

    except ValueError:
        if count == "":
            count = 1
        else:
            print("Please choose number from 1 to 1000.")
            sys.exit(2)

    if count not in range(1,1001):
        print("Please choose number from 1 to 1000.")
        sys.exit(2)

    # Gender settings
    gender = input("Choose gender (m)ale / (f)emale / (r)andom (default: (r)andom): ").upper()
    if gender not in["M", "F", "R", ""]:
        print("Wrong choice. Please try again.")
        sys.exit(2)

    elif gender in ["R", ""]:
        gender = None

    generate_names(count, gender)

if __name__ == "__main__":
    locale.setlocale(locale.LC_TIME, "")
    main()
