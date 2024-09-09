#!/usr/bin/env python3
"""
Author : jloe <jloe@sandia.gov>
Date   : 2021-02-11
Purpose: Play Telephone.
"""

import argparse
import os
import random
import string
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Play Telephone.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('message',
                        metavar='str',
                        help='A message or a file with message.')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations.',
                        metavar='float',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed.',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.message):
        args.message = open(args.message,'r').read().rstrip()

    if(args.mutations > 1 or args.mutations < 0):
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """What is the message?"""

    args = get_args()
    msg = args.message
    random.seed(args.seed)

    num_mutations = round(args.mutations * len(msg))
    bank = ''.join(sorted(string.ascii_letters + string.punctuation))

    indices = random.sample(range(len(msg)),num_mutations)
    
    newStr = ''
    #for k in indices
        #newStr = msg[:k] #no... That overwrites earlier stuff.  
    
    for k in range(len(msg)):
        if k in indices:
            new_char = random.choice(bank.replace(msg[k],''))
        else:
            new_char = msg[k]
        newStr += new_char
    
    print(f'You said: "{msg}"')
    print(f'I heard : "{newStr}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
