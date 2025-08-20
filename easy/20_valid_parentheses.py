"""
LeetCode Problem 20: Valid Parentheses
Difficulty: Easy

Problem Statement:
------------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
---------
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Solution:
---------
We use a stack to keep track of opening brackets.
- When encountering an opening bracket, push it onto the stack.
- When encountering a closing bracket, check if it matches the top element of the stack.
- If not, the string is invalid.
- At the end, if the stack is empty, the string is valid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

"""
Time Complexity: O(n)
- We scan the string once and each push/pop operation takes O(1).

Space Complexity: O(n)
- In the worst case (all opening brackets), we store all n characters in the stack.
"""
