# Solution 1 for LeetCode "Count and Say" problem.
# Description:
#   The count-and-say sequence is a sequence of digit strings defined by the
#   recursive formula
#    - countAndSay(1) = "1"
#    - countAndSay(n) is the run-length encoding of countAndSay(n-1).
#   Given a positive integer n, return the nth element of the count-and-say sequence.

## Solution uses recursion, which instead of building from the bottom up, we
## define the base case n == 1 -> "1"; recursively get the result for n - 1;
## "Say" that result to produce current term.

def countAndSay(self, n: int) -> str:
  # Base case: the first term in the sequence
  if n == 1:
    return "1"

  # Recursively get the previous term
  prev = self.countAndSay(n - 1)

  # Process previous term to generate the current one
  result = ""
  count = 1      # count of consecutive characters

  # Traverse the previous string
  for i in range(1, len(prev)):

    # If same digit as previous, increase count
    if prev[i] == prev[i - 1]:
      count += 1
    else:
      # Different digit -> append count and digit
      result += str(count) + prev[i - 1]
      count = 1       # reset count

  # Don't forget to append the last group
  result += str(count) + prev[-1]

  return result
