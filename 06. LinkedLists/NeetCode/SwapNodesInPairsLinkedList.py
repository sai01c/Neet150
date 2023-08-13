"""
https://leetcode.com/problems/swap-nodes-in-pairs/

approach - just manipulating the pointers

tc - n
sc - 1

instead, we can just use reverse nodes in K groups to do this

"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        dummy = ListNode()
        prev = dummy
        prev.next = head
        
        while first and first.next:
            second = first.next
            third = second.next
            
            prev.next = second
            second.next = first
            first.next = third
            
            prev = first
            first = third
        
        return dummy.next

            
            