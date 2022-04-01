#!/usr/bin/env python3

# Created by: Huzaifa
# Created on: March 2022
# This function takes a random integer between 0-9
# and tells the user if they guessed corretly

import random


def main():
    # this function takes a random integer between 0-9
    # and tells the user if they guessed corretly

    # input
    user_guess = int(input("Insert any number between 0-12 (integers): "))
    print("")

    # process and output
    if user_guess == 1:
        print("The month is January")
    elif user_guess == 2:
        print("The month is February")
    elif user_guess == 3:
        print("The month is March")
    elif user_guess == 4:
        print("The month is April")
    elif user_guess == 5:
        print("The month is May")
    elif user_guess == 6:
        print("The month is June")
    elif user_guess == 7:
        print("The month is July")
    elif user_guess == 8:
        print("The month is August")
    elif user_guess == 9:
        print("The month is September")
    elif user_guess == 10:
        print("The month is October")
    elif user_guess == 11:
        print("The month is November")
    elif user_guess == 12:
        print("The month is December")
    else:
        print("Sorry big man I got nothing ¯\_(ツ)_/¯ ")


if __name__ == "__main__":
    main()
