# Solution 1: Using expand around center approach

def longestPalindrome(self, s: str) -> str:
  """
  Solution #1 for LeetCode "Longest Palindromic String" problem.
  Given a string s, return the longest palindromic substring in s.
  
  @args: s, a string
  @returns: string of longest palindrome found in s

  Complexity: 
  Time: O(n^2)
  Space: O(1)
  """
  def expand(left, right):
    """
    Expands around a given center and returns the length of the palindrome found.

    @args: left, right - index values for character in s
    @returns: length of palindrome found, an int
      
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
      # Move left pointer left and right pointer right, for outward expansion
      left -= 1
      right += 1

      # Length of palindrome
      return right - left - 1

    # Edge case: Empty string
    if not s:
      return ""

    # Initialise start and end to 0
    start, end = 0

    # Loop through string characters
    for i in range(len(s)):
      # Odd-length palindrome (single center)
      len1 = expand(i, i)

      # Even-length palindrome (two centers)
      len2 = expand(i, i + 1)

      # Choose the maximum length found
      max_len = max(len1, len2)

      # Update result if longer palindrome is found
      if max_len > (end - start):
        start = i - (max_len - 1) // 2
        end = i + max_len // 2

  # Return substring containing longest palindrome
  return s[start:end + 1]
  
      
    
