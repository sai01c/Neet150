"""
https://leetcode.com/problems/reverse-linked-list/

Approach: Iterative - this is better understood if written on notes.
First, we shift the pointer from current to previous. 
Now, current becomes prev and the actual next (temp) becomes current
 
TC O(n) as we are visiting all the nodes once
SC O(1) 

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            temp = curr.next  # storing the variable
            curr.next = prev  # shifting the pointer
            prev = curr #prev should be assigned first
            curr = temp
        return prev
