# Solution 2 for LeetCode "Count and Say" problem.
# Description:
#   The count-and-say sequence is a sequence of digit strings defined by the
#   recursive formula
#    - countAndSay(1) = "1"
#    - countAndSay(n) is the run-length encoding of countAndSay(n-1).
#   Given a positive integer n, return the nth element of the count-and-say sequence.

## Solution uses iterative approach.

def countAndSay(self, n: int) -> str:
  # Start with the first term in the sequence
  result = "1"

  # Generate the sequence up to the nth term
  for _ in range(n - 1):
    next_string = ""        # This will store the next term
    i = 0                   # Pointer to traverse current string

    while i < len(result):
      # Start counting occurrences of the current digit
      count = 1

      # Count how many times the same digit repeats consecutively
      while i + 1 < len(result) and result[i] == result[i + 1]:
        count += 1
        i += 1

        # Append the count and digit to the next string
        next_string += str(count) + result[i]

        # Move to the next new digit
        i += 1

      # Update result for next new digit
      result = next_string

    # Return the nth term
    return result
