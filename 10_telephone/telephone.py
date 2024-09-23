#! /usr/bin/env python3
"""
Author: Jennifer Loe
Date: 9/20/24
Purpose: Play telephone with the computer
"""

import argparse
import os
import random
import string


def main():
    args = get_args()
    random.seed(args.seed)
    num_changes = round(args.mutations * len(args.text))
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    text = list(args.text)
    rand_idxs = random.sample(range(len(args.text)),num_changes)
    for i in range(len(rand_idxs)): 
        text[rand_idxs[i]] = random.choice(alpha.replace(text[rand_idxs[i]],''))
    print(f'You said: "{args.text}"')
    print(f'I heard : "{"".join(text)}"')

    
def get_args():
    parser = argparse.ArgumentParser(description="Mutate a string.", 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text",
                        type=str,
                        help="Text input or file to read.")
    parser.add_argument('-m',
                        '--mutations',
                        type=float,
                        metavar='percent',
                        help="Percentage (as a decimal between 0 and 1) of text to be mutated.",
                        default=0.1)
    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        metavar="seed",
                        help="Seed for random generator.",
                        default=None)
    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text) as fh:
            args.text = fh.read().rstrip()
            
    # if args.mutations < 0 or args.mutations > 1:
    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1.')
    return args
    
    
if __name__ == "__main__":
    main()