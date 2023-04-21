# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        dummy = ListNode(None)
        prev = dummy
        prev.next = slow
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        prev.next = temp
        return dummy.next