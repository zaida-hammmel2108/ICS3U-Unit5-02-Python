#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Nov 2022
# This program calculates the area of a triangle.

import random


def area_triangle(int_base, int_height):

    # process
    area = int_base * int_height / 2

    # output
    print("The area is: {0} cm².".format(area))


def main():
    # input
    str_base = input("Enter the base of the triangle: ")
    str_height = input("Enter the height the of triangle: ")

    try:
        int_base = int(str_base)
        int_height = int(str_height)
        # call functions
        area_triangle(int_base, int_height)
    except ValueError:
        print("Invalid integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
