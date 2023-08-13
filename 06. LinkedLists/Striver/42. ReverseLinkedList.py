"""
https://leetcode.com/problems/reverse-linked-list/

Approach - recursive solution

tc - n
sc - n recursive stack

"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nextHead = head
        if head.next:
            nextHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return nextHead