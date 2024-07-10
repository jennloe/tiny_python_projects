#! /usr/bin/env python3
"""
Author: Jennifer Loe
Date: 7/4/24
Purpose: Encode numbers with "jump the 5" algorithm.
"""

import argparse


def main():
    """Encode the message."""
    args = get_args()
    message = args.message
    code_dict = {'0': '5', '1': '9', '2': '8', '3': '7', '4': '6',
                 '5': '0', '6': '4', '7': '3', '8': '2', '9': '1'}
    
    # # Version 1: 
    # new_msg = ""
    # for char in message:
    #     if char.isnumeric():
    #         char = code_dict[char]
    #     new_msg += char
    # print(f"{new_msg}")

    # # Version 3: Doesn't work because overwrites itself. 
    # for char in set(message):
    #     if char in code_dict:
    #         message = message.replace(char,code_dict[char])
    # print(message)

    # Version 2: 
    # new_msg = [code_dict[c] if c.isnumeric() else c for c in message]
    # print(''.join(new_msg))

    # Version 2.5: 
    # print(''.join(code_dict[c] if c.isnumeric() else c for c in message))
    
    # This version prints a generator, so it doesn't work. 
    # print(code_dict[c] if c.isnumeric() else c for c in message)

    # # Version from book
    # for c in message:
    #     print(code_dict.get(c,c),end='')
    # print()

    # other version from book
    # print(''.join(code_dict.get(c,c) for c in message))

    # Cool trick from book
    print(message.translate(str.maketrans(code_dict)))

def get_args():
    """Get arguments."""
    parser = argparse.ArgumentParser(
        description="Encode numbers with jump 5 algorithm.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("message", help="Message to encode.", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    main()
