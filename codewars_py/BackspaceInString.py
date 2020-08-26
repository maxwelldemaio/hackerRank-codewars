"""
Assume "#" is like a backspace in string. 
This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""

def clean_string(myString):
    newString = ""
    for x in range(0, len(myString)):
        # Check if hash symbol encountered
        if (myString[x] == "#"):
            # Pop item from newString
            newString = newString[:-1]
        else:
            newString += myString[x]

    return newString


# Test Cases
assert clean_string('abc#d##c') == "ac", "Output isn't correct"
assert clean_string('abc####d##c#') == "", "Output isn't correct"
assert clean_string("#######") == "", "Output isn't correct"
assert clean_string("") == "", "Output isn't correct"
