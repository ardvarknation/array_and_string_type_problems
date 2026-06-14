# Solution to LeetCode "Valid Sudoku" problem.
# Description:
#    To determine if a 9x9 Sudoku board is valid:
#    -  Each row must contain the digits 1-9 without repetition
#    -  Each column must contain the digitis 1-9 without repetition.
#    -  Each of the 3x3 grid boxes must contain the digits 1-9 without repetition.

from collections import List, Set

def isValidSudoku(self, board: List[List[str]]) -> bool:
  """
  Function which receives a grid representation of a 9x9 Sudoku board,
  with values occupying every individual box, and determines whether the 
  game is completed correctly or not.

  @args: board, a List of Lists with str values 1-9
  @returns: Boolean True if correctly completed, False otherwise
  """
  # Check rows and columns
  for i in range(9):
    rowSet = set()
    colSet = set()

  for j in range(9):
    # Check each row in the grid
    if board[i][j] != '.':
      if board[i][j] in rowSet:
        return False
      rowset.add(board[i][j])

  # Check 3x3 subgrids
  for boxRow in range(3):
    for boxCol in range(3):
      boxSet = set()
      for i in range(3):
        for j in range(3):
          row = boxRow * 3 + i
          col = boxCol * 3 + j
          value = board[row][col]
        if value != '.':
          if value in boxSet:
            return False
          boxSet.add(value)

  # Board completed correctly
  return True
  
    
