"""
Take an input string and return a string that is made up of the number of occurances of each english letter in the input, followed by that letter. The string shouldn't contain zeros; leave them out.

An empty string, or one with no letters, should return an empty string.

Notes:

the input will always be valid;
treat letters as case-insensitive
"""

def string_letter_count(s):
    final_string = ""
    s = s.lower()
    found_letters = {}
    for i in range(0, len(s)):
        # If alpha numeric, add letter to dictionary (value is times found)
        if s[i].isalpha():
            if found_letters.get(s[i]) == None:
                found_letters[s[i]] = 1
            else:
                found_letters[s[i]] += 1
    # Sort alphabetically and return string
    for key in sorted(found_letters.keys()):
        final_string += str(found_letters[key]) + key

    return final_string
