#! /usr/bin/env python3
"""
Author: Jennifer Loe
Date: 9/25/24
Purpose: Sing 12 days of Xmas
"""

import argparse
import sys

def main():
    args = get_args()
    print('\n\n'.join([verse(i) for i in range(1,args.num+1)]), file=args.outfile)

def verse(day):
    ordinal = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
               7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth"}
    phrase = ["A partridge in a pear tree.",
              "Two turtle doves",
              "Three French hens",
              "Four calling birds",
              "Five gold rings",
              "Six geese a laying",
              "Seven swans a swimming",
              "Eight maids a milking",
              "Nine ladies dancing",
              "Ten lords a leaping",
              "Eleven pipers piping",
              "Twelve drummers drumming"]
    # Mine:
    # myverse = f"On the {ordinal[day]} day of Christmas,\nMy true love gave to me,\n"
    # myverse += ',\n'.join([phrase[i-1] for i in range(day,1,-1)])
    # myverse += ("A " if day == 1 else ",\nAnd a ") + f"{phrase[0]}."
    # return myverse
    # Alternate: 
    phrase_list = [f"On the {ordinal[day]} day of Christmas", 
              "My true love gave to me"]
    phrase_list.extend(reversed(phrase[:day]))
    if day > 1:
        phrase_list[-1] = "And " + phrase[0].lower()
    return ',\n'.join(phrase_list)


def get_args():
    parser = argparse.ArgumentParser(description="Sing the n days of Christmas",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--num',
                        type=int,
                        metavar="days",
                        help="Number of days to sing",
                        default=12)
    parser.add_argument('-o',
                        '--outfile',
                        type=argparse.FileType('wt'),
                        help="Output file.",
                        default=sys.stdout)
    args = parser.parse_args()
    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    return args

if __name__ == "__main__":
    main()