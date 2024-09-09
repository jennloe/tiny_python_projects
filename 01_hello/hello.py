#!/usr/bin/env python3
"""
Author: Jennifer Loe <jloe@sandia.gov>
Date: 2/4/21
Purpose: Say hello.
"""

import argparse  # parses arguments


# --------------------------------------------------------------
def get_args():
    """ Get command-line arguments."""
    parser = argparse.ArgumentParser(description='Say hello.')
    parser.add_argument('-n', '--name', metavar='name',
                        help='Name to greet', default='World')
    return parser.parse_args()


# -------------------------------------------------------------
def main():
    """ Execute 'hello world' """
    args = get_args()
    print('Hello, ' + args.name + '!')


# -------------------------------------------------------------
if __name__ == '__main__':
    main()
