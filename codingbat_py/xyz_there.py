"""
xyz_there


Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""


def xyz_there(str):
  if str[:3] == "xyz":
    return True
  for char in range(1, len(str)-2):
      if str[char:char+3] == "xyz" and str[char-1] != ".":
        return True
  return False
