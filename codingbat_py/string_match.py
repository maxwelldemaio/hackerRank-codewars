"""
string_match


Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""


def string_match(a, b):
  count = 0
  for x in range(len(a)-1):
    substringA = a[x:x+2]
    substringB = b[x:x+2]
    if substringA == substringB:
      count += 1
  return count
