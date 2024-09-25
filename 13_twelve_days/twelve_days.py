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
    print("Hellow xmas")
    print(f"{args.num} days of Christmas")

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
        parser.error(f'--num {"args.num"} must be between 1 and 12')
    return args

if __name__ == "__main__":
    main()