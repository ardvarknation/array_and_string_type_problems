# Solution 3: Brute-Force.

def longestPalindrome(self, s: str) -> str:
  """
  Solution for LeetCode "Longest Palindromic String" problem.
  Given a string s, return the longest palindromic substring in s.
  
  Approach uses Brute-Force to check every substring to find longest palindrome. 
  @args: s, a string
  @returns: string containing longest palindrome or empty string

  Complexity:
  Time: O(n^3)
  Space: O(1)  
  """
  def is_palindrome(sub):
    """
    Helper function to check if a substring is a palindrome.
    """
    return sub == sub[::-1]

  n = len(s)
  longest = ""

  # Check all substrings
  for i in range(n):
    for j in range(i, n):
      substring = s[i:j+1]

      # Check palindrome
      if is_palindrome(substring) and len(substring) > len(longest):
        longest = substring

  # Return longest palindrome found
  return longest
