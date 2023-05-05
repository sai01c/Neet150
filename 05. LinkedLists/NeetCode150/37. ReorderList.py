"""
https://leetcode.com/problems/reorder-list/

Approach: divide the linked list into two halves.
use two pointer slow and fast to find out the midle 
First half should be normal and second should be reversed. 
merge both the halves. 

Tc: O(n) we are iterating multiple times but it is n+n+n
Sc: O(1) dummy node does not depend on size of input
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
        slow = fast = dummy 
        #to find the middle element of linked list
        # 1-2-3-4-5 we need middle at 3
        # 1-2-3-4 we need middle at 2
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
        first = head #assign first to initial head
        second = prev
        while second: #merging first and second half
            a = first.next
            b = second.next
            first.next = second
            second.next = a
            first = a
            second = b