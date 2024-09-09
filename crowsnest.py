#!/usr/bin/env python3
"""
Author : jloe <jloe@sandia.gov>
Date   : 2021-02-04
Purpose: Find objects in the sea
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- Choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """What did we see in the sea?"""

    args = get_args()
    seaObj = args.word

    #article = 'a'
    # vowels = ['a','e','i','o','u','A','E','I','O','U']
    # if seaObj[0] in vowels:

    # Better version: 
    #if seaObj[0].lower() in 'aeiou':
        #article = 'an'

    # Shorter version:
    article = 'an' if seaObj[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {seaObj} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
