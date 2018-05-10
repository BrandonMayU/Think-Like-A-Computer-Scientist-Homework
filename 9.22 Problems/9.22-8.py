# Write a function that removes all occurrences of a given letter from a string.
import re

def remove_vowels(string, lettersToRemove):

    remove = lettersToRemove
    charsToRemove = ""
    for x in string:
        if x not in remove:
            charsToRemove += x
    return charsToRemove




print(remove_vowels("Brandon Mayhew", "aeioruAEIOUw"))