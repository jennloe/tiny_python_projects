#!/usr/bin/env python3
"""
# Author: Jennifer Loe
# Purpose: Say hello.
"""

import argparse


def main():
    """ " Main here"""
    args = get_args()
    print("Hello, " + args.name + "!")


# ---------------------------------------------------------------------
def get_args():
    """Get Args."""
    parser = argparse.ArgumentParser(description="Say Hello.")
    parser.add_argument(
        "-n", "--name", help="Name to greet.", metavar="name", default="World"
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
