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
    file = args.file[0]
    letters = [s.upper() for s in args.letters]
    abc_dict = {}
    for line in file:
        abc_dict[line[0].upper()] = line
    for my_letter in letters: 
        line = abc_dict.get(my_letter)
        if line: 
            print(line.rstrip())
        else:
            print(f'I do not know "{my_letter}".')

        
def get_args():
    parser = argparse.ArgumentParser(description="Give a file and letters from which to extract lines.",
                                     formatter_class= argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('letters', nargs='+', help= "One or more letters to look up.")
    parser.add_argument('--file', type=argparse.FileType('rt'), nargs=1, default=['gashlycrumb.txt'],
                        help= "Name of file to reference. Each line must start with a unique letter.")
    return parser.parse_args()

if __name__ == "__main__": 
    main()
