#! /usr/bin/env python3
'''
Author: Jennifer Loe
Date: 9/13/24
Purpose: Make up silly apple songs.
'''
import argparse
import os


def main():
    """
    User gives a vowel; we make it a song.
    """
    args = get_args()

    v = args.vowel
    text = args.text

    # Solution 1: 
    # for x in text:
    #     if x in 'aeiou':
    #         print(v.lower(), end='')
    #     elif x in 'AEIOU':
    #         print(v.upper(), end='')
    #     else:
    #         print(x,end='')
    # print()

    # Solution 1.5: 
    # new = ''
    # for x in text:
    #     if x in 'aeiou':
    #         new += v
    #     elif x in 'AEIOU':
    #         new += v.upper()
    #     else:
    #         new += x
    # print(new)

    # Solution 2: 
    # print(''.join([v if x in 'aeiou' else v.upper() if x in 'AEIOU' else x for x in text]))
    
    # Solution 2.5:
    # def new_char(x):
    #     # Note this function uses v that already exists in main. 
    #     return v if x in 'aeiou' else v.upper() if x in 'AEIOU' else x
    # print(''.join(new_char(x) for x in text))

    # Solution 3:
    # new = text
    # for x in 'aeiou':
    #     new = new.replace(x,v)
    # for x in 'AEIOU':
    #     new = new.replace(x,v.upper())
    # print(new)
    
    # Solution 3.5:
    # new = text
    # for x in 'aeiou':
    #     new = new.replace(x,v).replace(x.upper(), v.upper())
    # print(new)

    # Solution 4:
    # V = v.upper()
    # jump = {'a':v, 'e':v, 'i':v, 'o':v, 'u': v, 'A':V, 'E':V, 'I':V, 'O':V, 'U':V}
    # print(text.translate(str.maketrans(jump)))
    
    # Solution 4.5
    # V = v.upper()
    # # Put in two strings, and it makes the dictionary for you. v*5 = 'vvvvv'
    # print(text.translate(str.maketrans('aeiouAEIOU', v*5 + V*5)))

    # Solution 5: 
    # def new_char(x):
    #     # Note this function uses v that already exists in main. 
    #     return v if x in 'aeiou' else v.upper() if x in 'AEIOU' else x
    # # Note that map expects a list, so 'text' will be coerced into a list. 
    # print(''.join(map(new_char,text)))
    
    # Solution 5.5: 
    # print(''.join(map(lambda x: v if x in 'aeiou' else v.upper() if x in 'AEIOU' else x, text)))
    
    # Solution 6:
    # import re
    # text = re.sub('[aeiou]',v,text)
    # text = re.sub('[AEIOU]',v.upper(),text)
    # print(text)
    
    # Solution 6.5: 
    import re
    print(re.sub('[aeiou]',v, re.sub('[AEIOU]',v.upper(),text)))

def get_args():
    """
    Get input args from user. 
    """
    parser = argparse.ArgumentParser(description= "Give a vowel and text to make a silly song.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text",
                        type = str,
                        help="Text or name of file.")
    parser.add_argument("-v","--vowel",
                        type=str,
                        help="The vowel to substitute.",
                        default='a',
                        choices=list('aeiou'))
                        #choices=['a','e','i','o','u'])
    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text) as fh:
            args.text = fh.read()
    return args


if __name__ == "__main__":
    main()
