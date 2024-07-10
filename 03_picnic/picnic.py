#! /usr/bin/env python3
"""
Author: Jennifer Loe
Date: 6/30/24
Purpose: To list items to take on a picnic. 
"""

import argparse


def main():
    """ Tell the user what items they are bringing. 
    """
    args = get_args()
    items = args.items
    if(args.sorted):
        items.sort()
    num_items = len(args.items)
    if num_items == 1:
        print(f"You are bringing {items[0]}.")
    elif num_items == 2:
        print(f"You are bringing {items[0]} and {items[1]}.")
    else:
        str = "You are bringing "
        for  i in range(num_items-1):
            str += f"{items[i]}, "
        str += f"and {items[-1]}."
        print(str)


def get_args():
    """ Parse arguments from user. """
    parser = argparse.ArgumentParser(description="List items for picnic.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("items", type=str, help="Any number of items for the picnic.", nargs='+')
    parser.add_argument('-s', '--sorted', help="Sort the items on the list.",action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    main()