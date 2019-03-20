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
