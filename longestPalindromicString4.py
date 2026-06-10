# Solution 4: Manacher's Algorithm.

def longestPalindrome(self, s: str) -> str:
  """
  Solution 4 for LeetCode "Longest Palindromic String" problem.
  Applies Manacher's Algorithm to solve problem.

  @args: s, a string
  @returns: string containing longest palindrome or empty string

  Complexity:
  Time: O(n)
  Space: O(n)
  """

  # Transform string input to handle even-length palindromes
  # Example: "abba" -> "#a#b#b#a#"
  t = '#' + '#'.join(s) + '#'
  n = len(t)

  # Array to store palindrome radius
  P = [0] * n

  # Center and right boundary
  center = 0
  right = 0

  for i in range(n):
    mirror = 2 * center - i      # mirror index of i

    # Initialise P[i] using mirror information
    if i < right:
      P[i] = min(right - i, P[mirror])

    # Expand around center i
    while (i - P[i] - 1 >= 0 and
           i + P[i] + 1 < n and
           t[i - P[i] - 1] == t[i + P[i] + 1]):
             P[i] += 1

    # If palindrome centered at i expands past right,
    # adjust center and right boundary
    if i + P[i] > right:
      center = i
      right = i + P[i]

# Find the maximum palindrome length
max_len = max(P)
center_index = P.index(max_len)

# Extract the substring from the original string and return
start = (center_index - max_len) // 2
return s[start:start + max_len]


