"""
string_splosion

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""


def string_splosion(str):
  y = []
  for x in range(len(str) + 1):
    y.append(str[0:x])
  return ''.join(y)


print(string_splosion('Code'))
