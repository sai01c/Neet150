"""
https://leetcode.com/problems/reorder-list/

Approach: divide the linked list into two halves.
use two pointer slow and fast to find out the mid 
First half should be normal and second should be reversed. 
merge both the halves. 

Tc: O(n) we are iterating multiple times but it is n+n+n
Sc: O(n)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy #to find the middle element of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next 
        slow.next = None #we are ending first half here
        prev = None
        while second: #reversing second list here
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first = head
        second = prev
        while second: #merging first and second half
            a = first.next
            b = second.next
            first.next = second
            second.next = a
            first = a
            second = b