"""
https://leetcode.com/problems/linked-list-cycle/

Approach: we shall two pointers slow and fast. 
slow moves by one node and fast moves by two nodes. 
if there is a cycle at one point both will be equal. 

TC: O(n) iterating once
SC: O(1) only pointers
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False

