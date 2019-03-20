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
