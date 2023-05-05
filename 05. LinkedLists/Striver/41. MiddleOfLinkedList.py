"""
https://leetcode.com/problems/middle-of-the-linked-list/

Approach - just go to middle of the linked list using slow and fast pointers

tc - n
sc - 1
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.next