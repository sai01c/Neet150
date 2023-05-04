"""
https://leetcode.com/problems/odd-even-linked-list/

approach - create two dummy nodes and attach them to first and second nodes.
now increase the pointers by two nodes and attach them

tc
sc
"""

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy2 = ListNode(0)
        first = head
        second = first.next
        dummy.next = first
        dummy2.next = second
        
        while first and first.next and second and second.next:
            #increase by 2 because we need alternate nodes
            temp2 = second.next.next
            temp = first.next.next
            
            #join them
            first.next = temp
            second.next = temp2
            
            #increase the pointers
            first = first.next
            second = second.next
            
        #join the first to second
        first.next = dummy2.next
        return dummy.next

        