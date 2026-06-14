# Solution for the LeetCode problem "Isomorphic Strings".
# Description:
#    Two strings, s and t, are isomorphic if the characters in s can be replaced to get t.
#    All occurrences of a character must be replaced with another character while preserving
#    the order of characters.

def isIsomorphic(self, s: str, t: str) -> bool:
  """
  Function returns True if a string s and string t are isomorphic,
  or False otherwise.

  @args: s and t, str
  @returns: Boolean True/False  
  """
  # Check for cases where s and t are different lengths making output False.
  if len(s) != len(t):
    return False

  s_to_t = {}        # for s --> t mapping
  t_to_s = {}        # for t --> s mapping

  # Compare two characters - one from each string - at a time.
  for char_s, char_t in zip(s, t):
    if char_s in s_to_t:
      if s_to_t[char_s] != char_t:
        return False

    else:
      s_to_t[char_s] = char_t

    if char_t in t_to_s:
      if t_to_s[char_t] != char_s:
        return False

    else:
      t_to_s[char_t] = char_s

  return True
