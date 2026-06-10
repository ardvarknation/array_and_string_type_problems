# Solution 2: Using Dynamic Programming approach.

def longestPalindrome(self, s: str) -> str:
  """
  Solution 2 for LeetCode "Longest Palindromic String" problem, which applies DP approach.
  DP Approach: dp[i][j] == True if substring s[i:j+1] is a palindrome.

  @args: s, a string 
  @returns: string of longest palindrome, or empty string

  Complexity:
  Time: O(n^2)
  Space: O(n^2)  
  """
  n = len(s)

  # Edge case: Empty string
  if n == 0:
    return ""

  # Create a DP table initialised to False
  dp = [[False] * n for _ in range(n)]

  # Initialise start/max_len pointers
  start = 0
  max_len = 1

  # Every single character is a palindrome
  for i in range(n):
    dp[i][i] = True

  # Check substrings of length >= 2
  for length in range(2, n + 1):
    for i in range(n - length + 1):
      j = i + length - 1

      # Check if first and last characters match
      if s[i] == s[j]:
        if length == 2:
          # Two character palindrome
          dp[i][j] = True
        else:
          # Expand inner substring
          dp[i][j] = dp[i + 1][j - 1]

        # Update longest palindrome
        if dp[i][j] and length > max_len:
          start = i
          max_len = length

  # Return substring of longest palindrome
  return s[start:start + max_len]
