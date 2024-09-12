#! /usr/bin/env python3
"""
Author: Jennifer Loe
8/10/24
Purpose: Count Words
"""
import argparse
import sys

def main():
    """ Count the words! """
    args = getArgs()
    files = args.file

    total_lc, total_wc, total_bc = 0, 0, 0
    for file_handle in files:
        lc, wc, bc = 0, 0, 0
        for line in file_handle:
            lc += 1
            wc += len(line.split())
            bc += len(line)
        print(f'{lc:8}{wc:8}{bc:8} {file_handle.name}')
        total_lc += lc
        total_wc += wc
        total_bc += bc
    if len(files) > 1:
        print(f'{total_lc:8}{total_wc:8}{total_bc:8} total')


# ---------------------------------------------------
def getArgs():
    """ Get Args """
    parser = argparse.ArgumentParser(description="Count Words",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("file",
                        nargs='*',
                        help="Input file(s) or text.",
                        type = argparse.FileType('rt'), # This returns a list of open file handles.
                        default=[sys.stdin])
    return parser.parse_args()

if __name__ == "__main__":
    main()
    