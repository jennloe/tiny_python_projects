#! /usr/bin/env python3

"""
Author: Jennifer Loe
Date: 9/20/24
Purpose: Sing the annoying bottles song.
"""

import argparse

def main():
    args = get_args()

    # could also do reversed(range(args.num+1))
    for n in range(args.num,0,-1):
        print(get_verse(n))
        
def get_verse(n):
    end = (f"{n-1} bottle{'s' if n - 1 > 1 else ''} of beer on the wall!\n" 
            if n-1 > 0 else f"No more bottles of beer on the wall!")
    return (f"{n} bottle{'s' if n > 1 else ''} of beer on the wall,\n"
            f"{n} bottle{'s' if n > 1 else ''} of beer,\n"
            f"Take one down, pass it around,\n" + end)
            


def get_args():
    """ Get Arguments """
    parser = argparse.ArgumentParser(description="Sing bottles on the wall.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--num',
                        type=int,
                        metavar="bottles",
                        help="Number of bottles to start song with.",
                        default=10)
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args


if __name__ == "__main__":
    main()