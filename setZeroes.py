from typing import List

def setZeroes(self, matrix: List[List[int]]) -> None:
  """
  Solution for LeetCode "Set Matrix Zeroes" problem.
  Do not return anything, modify array in-place instead.
  @args: matrix = List[List[int]]
  @return: None
  
  Complexity:
  Space: O(1)  
  """
  # Get matrix dimensions
  m, n = len(matrix, len(matrix[0])

  # Step 1: Check if first row contains any zero
  firstRowHasZero = False
  for j in range(n):
    if matrix[0][j] == 0:
      firstColHasZero = True
      break

  # Step 2: Check if first column contains any zero
  firstColHasZero = False
  for i in range(m):
    if matrix[i][0] == 0:
      firstColHasZero = True
      break

  # Step 3: If matrix[i][j] == 0, mark it's row and column
  for i in range(1, m):
    for j in range(1, n):
      # If row or column is marked, set to zero
      if matrix[i][j] == 0:
        matrix[i][0] = 0    # mark the row
        matrix[0][j] = 0    # mark the column

  # Step 4: Set elements to 0 based on markers
  # Skip first row and column for now
  for i in range(1, m):
    for j in range(1, n):
      # If row or column is marked, set to zero
      if matrix[i][0] == 0 or matrix[0][j] == 0:
        matrix[i][j] = 0

  # Step 5: Zero out first row if needed
  if firstRowHasZero:
    for j in range(n):
      matrix[0][j] = 0

  # Step 6: Zero out first column if needed
  if firstColHasZero:
    for i in range(m):
      matrix[i][0] = 0
      
