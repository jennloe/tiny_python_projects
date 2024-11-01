#! /usr/bin/env python3
"""
Author: Jennifer Loe
10/6/24
Purpose: Make rhyming words
"""

import argparse
import string
import re


def main():
    """Get the rhyming words."""
    args = get_args()
    word = args.word.lower()

    beg, end = split_word(word)
    if beg == None:
        print(f'Cannot rhyme "{args.word}"')
        return
    consonants = list(string.ascii_lowercase)
    for x in list('aeiou'):
        consonants.remove(x) 
    letter_combos = consonants + \
                    str.split("bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st "
                    "sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr")
    if beg in letter_combos:
        letter_combos.remove(beg)
    letter_combos.sort()

    for x in letter_combos:
        print(x + end)

def split_word(word):
    word = word.lower()
    idx = [word.find(x) for x in 'aeiou']
    idx = [x for x in idx if x != -1]
    if idx == []:
        beg = None
        end = None
    else:
        idx = min(idx)
        beg = word[:idx]
        end = word[idx:]
    return beg, end

def test_splword():
    b, e = split_word('fled')
    assert b == 'fl'
    assert e == 'ed'
    b, e = split_word('apple')
    assert b == ''
    assert e == 'apple'
    b, e = split_word('cupcake')
    assert b == 'c'
    assert e == 'upcake'

def get_args():
    """Get arguments from user."""
    parser = argparse.ArgumentParser(description="Give word for which to get rhymes.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("word",
                        type=str,
                        help="A word to rhyme")
    return parser.parse_args()


if __name__ == "__main__":
    main()