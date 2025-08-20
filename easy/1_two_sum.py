"""
LeetCode Problem 1: Two Sum
Difficulty: Easy

Problem Statement:
------------------
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

- Each input will have exactly one solution.
- You may not use the same element twice.
- The answer can be returned in any order.

Examples:
---------
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] = 2 + 7 = 9

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Solution:
---------
We use a hashmap (dictionary in Python) to store numbers and their indices. 
For each number, check if the complement (target - num) exists in the hashmap.
If yes, return the pair of indices. Otherwise, store the current number in the hashmap.
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

"""
Time Complexity: O(n) 
- We traverse the array once, performing O(1) lookup for each element.

Space Complexity: O(n) 
- At most, we store all n elements in the hashmap.
"""
