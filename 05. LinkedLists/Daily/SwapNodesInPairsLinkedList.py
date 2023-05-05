"""
https://leetcode.com/problems/swap-nodes-in-pairs/

approach - just manipulating the pointers

tc - n
sc - 1

instead, we can just use reverse nodes in K groups to do this

"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        dummy.next = head
        curr = head
        
        while curr and curr.next:
            second = curr.next
            groupNext = curr.next.next
            
            second.next = curr
            curr.next = groupNext #not understood why we require this line
            prev.next = second
            
            prev = curr
            curr = groupNext
            
        return dummy.next