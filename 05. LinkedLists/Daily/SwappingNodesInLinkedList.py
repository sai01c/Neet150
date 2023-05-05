"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

Approach - 
have one loop for find the k element from the start
another loop for finding k element from the end.
swap those two elements

tc - n
sc - 1
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        start = head  # assigning head here but we considered start as a pointer?
        end = head
        temp = head
        i = 1
        while i < k:
            start = start.next
            i += 1
        total = 0
        while temp:
            temp = temp.next
            total += 1
        j = 0
        while j < total - k:
            end = end.next
            j += 1
        start.val, end.val = end.val, start.val
        return head
