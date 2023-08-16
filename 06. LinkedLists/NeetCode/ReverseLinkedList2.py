"""
https://leetcode.com/problems/reverse-linked-list-ii/
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(501, head)
        slow = dummy
        while left > 1 and slow:
            left -= 1
            slow = slow.next
        prevGroup = slow
        slow = slow.next
        fast = dummy
        while fast and right:
            right -= 1
            fast = fast.next
        nextGroup = fast.next
        fast.next = None
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        prevGroup.next = fast
        slow.next = nextGroup
        
        return dummy.next
        
        