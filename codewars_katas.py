"""
kyu 8. INSTRUCTIONS. Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it. "a" = 1, "b" = 2, etc.
"""

def alphabet_position(text):
    my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u":21, "v":22, "w": 23, "x": 24, "y": 25, "z": 26}
    string_to_nums = []
    
    for letter in text:
        if letter.lower() in my_dict.keys():
            string_to_nums.append(my_dict.get(letter.lower()))
        else:
            continue
    print(' '.join([str(i) for i in string_to_nums]))
    return ' '.join([str(i) for i in string_to_nums])
 
 """
 kyu 7. INSTRUCTIONS. An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. 
 Assume the empty string is an isogram. Ignore letter case.
 """
 
 def is_isogram(string):
    string_lowered = string.lower()
    counter = 0
    for letter in string_lowered:
        counter += string_lowered.count(letter)
    if counter > len(string):
        return False
    else:
        return True
 
"""
kyu 8. INSTRUCTIONS: ou might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive. Examples:
findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
"""
import math
def find_next_square(sq):
    if math.sqrt(sq).is_integer():
        return int((math.sqrt(sq) + 1) ** 2)
    else:
        return -1

"""
7kyu. INSTRUCTIONS: 
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

    each taken only once - coming from s1 or s2.

Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

def longest(s1, s2):
    longest_string=""
    uniqs1 = ""
    uniqs2 = ""
    for letter in s1:
        if letter in uniqs1:
            continue
        else:
            uniqs1 += letter
    
    for letter in s2:
        if letter in uniqs2:
            continue
        else:
            uniqs2 += letter
            
    for letter in uniqs2:
        if letter in uniqs1:
            continue
        else:
            uniqs1 += letter

    return "".join(sorted(uniqs1))
 
 
