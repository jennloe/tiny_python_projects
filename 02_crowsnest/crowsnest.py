#! /usr/bin/env python3
"""
Purpose: Report sightings from the crow's nest.
Author: Jennifer Loe
Date: 6/28/24
"""

import argparse


def main():
    """State what is seen from the crow's nest."""
    args = get_args()
    if args.word[0] in "aeiouAEIOU":
        article = "an"
    else:
        article = "a"
    print(f"Ahoy, Captain, {article} {args.word} off the larboard bow!")


def get_args():
    """Parse the arguments from the user."""
    parser = argparse.ArgumentParser(
        description="Tell the captain what is seen from the crow's nest"
    )
    parser.add_argument("word", help="Object or creature seen.")
    return parser.parse_args()


if __name__ == "__main__":
    main()
