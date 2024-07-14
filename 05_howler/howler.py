#! /usr/bin/env python3
"""
Author: Jennifer Loe
Date: 7-10-24
Purpose: Turn text into yelling. :)
"""

import argparse
import os

def main():
    args = get_args()
    text = args.input
    outfile = args.outfile

    if os.path.isfile(text):
        # Note: Don't use os.open! That's for low-level stuff!
        # fh = "file handle"
        fh = open(text)
        text = fh.read()
    if outfile:
        fh = open(outfile,'at')
        fh.write(text.upper() + "\n")
        fh.close()
    else:
        print(text.upper())

def get_args():
    parser = argparse.ArgumentParser(description="Turn text into yelling.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input', help="Text or text file to turn into yelling.", metavar='text')
    parser.add_argument('-o','--outfile',help="Name of file in which to save output.",metavar=str)
    return parser.parse_args()


if __name__ == "__main__":
    main()