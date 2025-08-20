"""
LeetCode Problem 53: Maximum Subarray
Difficulty: Medium

Problem Statement:
------------------
Given an integer array nums, find the subarray with the largest sum,
and return its sum.

Examples:
---------
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Solution (Kadane's Algorithm):
------------------------------
Maintain a running sum (curr_sum). For each number:
- Add it to curr_sum.
- If curr_sum becomes negative, reset it to 0 (start a new subarray).
- Track the maximum value seen so far in max_sum.
This yields the maximum subarray sum in one pass.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize to the smallest possible to handle all-negative arrays
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0

        return max_sum

"""
Time Complexity: O(n)
- Single pass through the array.

Space Complexity: O(1)
- Constant extra space.
"""
