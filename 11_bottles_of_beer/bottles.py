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
    print("\n\n".join(map(get_verse,range(args.num,0,-1))))
        
def get_verse(n):
    end = (f"{'No more' if n == 1 else n-1} bottle{'s' if n - 1 != 1 else ''} of beer on the wall!")
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
    
def test_verse():
    """Test verse"""
    last_verse = get_verse(1)
    assert last_verse == '\n'.join([
    '1 bottle of beer on the wall,', '1 bottle of beer,',
    'Take one down, pass it around,',
    'No more bottles of beer on the wall!'
    ])
    two_bottles = get_verse(2)
    assert two_bottles == '\n'.join([
    '2 bottles of beer on the wall,', '2 bottles of beer,',
    'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])