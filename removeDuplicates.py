# Solution 1 for LeetCode "Remove Duplicates from Sorted Array" problem.
# Description:
#  Given an integer array, nums, sorted in non-decreasing order, remove the duplicates in-place
#  such that each unique element appears only once.

def removeDuplicates(self, nums: List[int]) -> int:
  length = len(nums)
  if length == 0:
    return 0

  unique_index = 0  # tracks position of last unique element

  # start loop from second element
  for i in range(1, length):
    if nums[i] != nums[unique_index]:
      # when new value is found, move unique_index forward
      unique_index += 1
      # copy new value into that position
      nums[unique_index] = nums[i]

  # return the first unique index +1 which is unique length
  return unique_index + 1
