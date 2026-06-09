from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
  """
  Solution to LeetCode "3Sum" problem.
  Given an integer array nums, return all triplets that sum to 0.
  
  @args: nums - List[int]
  @returns: triplets - List[List[int]]
    
  Complexity:
  Time: O(n^2)
  Space: O(1) (excluding output)
  """
  # Start by sorting nums 
  nums.sort()
  triplets = [] 

  # Loop through nums
  for i in range(len(nums)):
    # Skip duplicate values for i
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    # Initialise left and right pointers
    left, right = i + 1, len(nums) - 1

    # Read from start and end/outside to middle of nums
    total = nums[i] + nums[left] + nums[right]

    # Search for next triplet
    if total == 0:
      triplets.append([nums[i], nums[left], nums[right]])

      # Skip duplicates 
      while left < right and nums[left] == nums[left + 1]:
        # Move left pointer right
        left += 1
        # Move right pointer left
        right -= 1

      # Ensure pointers continue looking while values remain untried
      left += 1
      right -= 1

    elif total < 0:
      # Move left pointer right
      left += 1
    else:
      # Move right pointer left
      right -= 1

  return triplets  
