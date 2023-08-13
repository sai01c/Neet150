"""
https://leetcode.com/problems/remove-linked-list-elements/

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode()
        prev = dummy
        prev.next = curr
        
        while curr:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
            prev = prev.next
            if curr:
                curr = curr.next
            
        return dummy.next
    

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0)
        dummy.next = curr
        prev = dummy
        while curr:
            temp = curr.next
            if curr.val == val:
                prev.next = temp
                curr = temp
            else:
                prev = curr
                curr = curr.next
                
        return dummy.next
        