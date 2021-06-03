#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 3, 2021
# This program has a function that accepts any level as a string and
# returns the mark as a percentage


def calc_mark(level_string):
    level_int = -1
    if level_string == "4+":
        level_int = 97
    elif level_string == "4":
        level_int = 90
    elif level_string == "4-":
        level_int = 83
    elif level_string == "3+":
        level_int = 78
    elif level_string == "3":
        level_int = 74
    elif level_string == "3-":
        level_int = 71
    elif level_string == "2+":
        level_int = 68
    elif level_string == "2":
        level_int = 64
    elif level_string == "2-":
        level_int = 61
    elif level_string == "1+":
        level_int = 58
    elif level_string == "1":
        level_int = 54
    elif level_string == "1-":
        level_int = 51
    else:
        level_int = -1
    return level_int


def main():
    # get the level from the user as a string
    user_level_string = input("Enter a level you want"
                              " converted as a percentage: ")

    # convert the level into a number
    user_level_int = calc_mark(user_level_string)

    if (user_level_int == -1):
        print("Error. {} is not a valid number". format(user_level_string))
    else:
        print("Level {} has a middle"
              " percentage of {}%". format(user_level_string, user_level_int))


if __name__ == "__main__":
    main()
