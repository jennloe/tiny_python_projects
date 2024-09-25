#! /usr/bin/env python3

"""
Author: Jennifer Loe
Date: 9/24/24
Purpose: Write a ransom note from the catnapper. :P
"""

import argparse
import os
import random


def main():
    """ Print the ransom note here. """
    args = get_args()
    random.seed(args.seed)
    print(''.join(map(lambda x: random.choice([x.lower(),x.upper()]),args.text)))


def get_args():
    """ Parse input arguments. """
    parser = argparse.ArgumentParser(description="Randomly capitalize letters of text.",
                                     formatter_class= argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                        help='Text or file to be randomly capitalized.',
                        type = str,
                        metavar='text')
    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        help="Seed for random generator.",
                        default=None)
    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text) as fh:
            args.text = fh.read().rstrip()
    return args


if __name__ == "__main__":
    main()