#! /usr/bin/env python3
'''
Author: Jennifer Loe
Date: 9/13/24
Purpose: Make up silly apple songs.
'''
import argparse
import os


def main():
    """
    User gives a vowel; we make it a song.
    """
    args = get_args()

    v = args.vowel
    text = args.text
    if os.path.isfile(text):
        fh = open(text)
        text = fh.read()
        fh.close 

    # Solution 1: 
    # for x in text:
    #     if x in 'aeiou':
    #         print(v.lower(), end='')
    #     elif x in 'AEIOU':
    #         print(v.upper(), end='')
    #     else:
    #         print(x,end='')
    # print()

    # Solution 1.5: 
    # new = ''
    # for x in text:
    #     if x in 'aeiou':
    #         new += v
    #     elif x in 'AEIOU':
    #         new += v.upper()
    #     else:
    #         new += x
    # print(new)

    # Solution 2: 
    # print(''.join([v if x in 'aeiou' else v.upper() if x in 'AEIOU' else x for x in text]))

    # Solution 3:
    new = text
    for x in 'aeiou':
        new = new.replace(x,v)
    for x in 'AEIOU':
        new = new.replace(x,v.upper())
    print(new)

def get_args():
    parser = argparse.ArgumentParser(description= "Give a vowel and text to make a silly song.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text",
                        type = str,
                        help="Text or name of file.")
    parser.add_argument("-v","--vowel",
                        type=str,
                        help="The vowel to substitute.",
                        default='a',
                        choices=['a','e','i','o','u'])
    return parser.parse_args()


if __name__ == "__main__":
    main()
