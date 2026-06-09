from typing import List

def setZeroes(self, matrix: List[List[int]]) -> None:
  """
  Solution 2 to LeetCode "Set Matrix Zeroes" problem.
  (Uses additional space to track rows and columns to zero out).
  Easier to understand but uses additional space.
  @args: matrix = List[List[int]]
  @returns: None

  Complexity: 
  Space: O(m + n)
  """
  m, n = len(matrix), len(matrix[0])

  # Step 1: Create sets to keep track of rows and columns with zeros
  zeroRows = set()
  zeroCols = set()

  # Step 2: Identify all rows and columns that contain zero
  for i in range(m):
    for j in range(n):
      if matrix[i][j] == 0:
        zeroRows.add(i)      # mark this row
        zeroCols.add(j)      # mark this column

  # Step 3: Update the matrix
  for i in range(m):
    for j in range(n):
      # If current row or column is marked, set to zero
      if i in zeroRows or j in zeroCols:
        matrix[i][j] = 0
  
