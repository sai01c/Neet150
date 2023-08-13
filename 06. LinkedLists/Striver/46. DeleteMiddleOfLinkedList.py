"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

approach - use two pointers slow and fast to go the middle of the linked list
have a prev pointer behind slow and skip slow after you reach middle

tc - n
sc - 1
"""

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