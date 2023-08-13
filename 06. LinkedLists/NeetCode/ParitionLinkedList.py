"""
https://leetcode.com/problems/partition-list/

Approach - 

tc
sc

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        dummy2 = ListNode()
        prev2 = dummy2
        
        curr = head
        while curr:
            if curr.val < x:
                prev.next = curr
                prev = prev.next
            else:
                prev2.next = curr
                prev2 = prev2.next
            curr = curr.next
        
        prev2.next = None    
        prev.next = dummy2.next
        return dummy.next
        