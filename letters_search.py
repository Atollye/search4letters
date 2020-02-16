#!/usr/bin/env python3

def search4letters(phrase, letters='aeiou'):
    """ Returns the set of vowels found in 'phrase'"""
    return set(letters).intersection(set(phrase))

if __name__ == "__main__":
    phrase = input()
    res = search4letters(phrase)
    print(str(res))
