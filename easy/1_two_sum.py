"""
1. Two Sum (LeetCode)

Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

-------------------------------------------------
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
-------------------------------------------------

Complexity Analysis:
- Time Complexity: O(n)
    We iterate through the list once, and dictionary lookups/inserts are O(1) on average.
- Space Complexity: O(n)
    We store up to n elements in the dictionary in the worst case.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            y = target - num
            if y in seen:
                return [seen[y], i]
            seen[num] = i
        return []

# ---------------------------
# Example runs
# ---------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))   # Output: [0, 1]
    print(sol.twoSum([3,2,4], 6))       # Output: [1, 2]
    print(sol.twoSum([3,3], 6))         # Output: [0, 1]
