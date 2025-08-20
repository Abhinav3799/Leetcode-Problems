"""
LeetCode Problem 21: Merge Two Sorted Lists
Difficulty: Easy

Problem Statement:
------------------
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new list.  
The new list should be made up of nodes from list1 and list2.

Examples:
---------
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Solution:
---------
We use a dummy node and a pointer `cur`.  
- Compare the heads of both lists, attach the smaller one to `cur.next`.  
- Move the pointer forward in the list from which the node was chosen.  
- Continue until one list is exhausted, then attach the remaining nodes.  
- Return `dummy.next` as the head of the merged sorted list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)   # Dummy node
        cur = d

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2
        return d.next

"""
Time Complexity: O(n + m)
- We traverse both linked lists once, where n and m are the lengths of list1 and list2.

Space Complexity: O(1)
- We only use a few pointers, no extra space apart from the output list nodes.
"""
