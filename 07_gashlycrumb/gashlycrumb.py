#! /usr/bin/env python3
"""
Author: Jennifer Loe
Date: 9/11/2024
Purpose: To recite bad poetry
"""
import argparse


def main():
    """
    Here is main.
    """

    args = get_args()
    letters = [s.upper() for s in args.letters]
    abc_dict = {}
    for line in args.file:
        abc_dict[line[0].upper()] = line.rstrip()
    for my_letter in letters:
        line = abc_dict.get(my_letter)
        if line:
            print(line)
        else:
            print(f'I do not know "{my_letter}".')


def get_args():
    """
    Parse and return arguments.
    """
    parser = argparse.ArgumentParser(
        description="Give a file and letters from which to extract lines.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("letters", nargs="+", help="One or more letters to look up.")
    parser.add_argument(
        "--file",
        "-f",
        type=argparse.FileType("rt"),
        # nargs=1, # DON'T put this because it makes you return a list.
        # argparse will always error with more than one
        # input if you didn't tell it to accept more than one.
        # So you don't need to specify this.
        default="gashlycrumb.txt",
        help="Name of file to reference. \
                              Each line must start with a unique letter.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
