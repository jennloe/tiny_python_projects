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
    if end == None:
        print(f'Cannot rhyme "{args.word}"')
        return
    consonants = list(string.ascii_lowercase)
    for x in list('aeiou'):
        consonants.remove(x)
    pattern = "["+''.join(consonants)+"]+"
    letter_combos = consonants + \
                    str.split("bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st "
                    "sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr")
    if beg in letter_combos:
        letter_combos.remove(beg)
    letter_combos.sort()

    for x in letter_combos:
        print(x + end)

def split_word(word):
    consonants = ''.join(re.findall(('[^aeiou]'),string.ascii_lowercase))
    res = re.match(f"([{consonants}]+)?([aeiou].*)",word.lower())
    if res: 
        return res.groups()[0], res.groups()[1]
    else:
        return None, None

def test_splword():
    assert split_word('fled') == ('fl','ed')
    assert split_word('apple') == (None,'apple')
    assert split_word('cupcake') == ('c','upcake')
    assert split_word('pwrt') == (None, None)
    assert split_word('123') == (None, None)
    assert split_word('CAT') == ('c','at')

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