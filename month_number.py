#!/usr/bin/env python3

# Created by: Huzaifa
# Created on: March 2022
# This function takes a random integer between 1-12 from the user
# and tells them what the month is accordingly

import random


def main():
    # This function takes a random integer between 1-12 from the user
    # and tells them what the month is accordingly

    # input
    user_guess = int(input("Insert any number between 1-12 (integers): "))
    print("")

    # process and output
    if user_guess == 1:
        print("it's January")
    elif user_guess == 2:
        print("it's February")
    elif user_guess == 3:
        print("it's March")
    elif user_guess == 4:
        print("it's April")
    elif user_guess == 5:
        print("it's May")
    elif user_guess == 6:
        print("it's June")
    elif user_guess == 7:
        print("it's July")
    elif user_guess == 8:
        print("it's August")
    elif user_guess == 9:
        print("it's September")
    elif user_guess == 10:
        print("it's October")
    elif user_guess == 11:
        print("it's November")
    elif user_guess == 12:
        print("it's December")
    else:
        print("Sorry big man I got nothing ¯\_(ツ)_/¯ ")
    print("\nDone")


if __name__ == "__main__":
    main()
