"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy
        while curr:
            while curr and curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr
            prev = prev.next
            curr = curr.next
                
        return dummy.next