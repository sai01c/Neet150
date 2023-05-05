"""
https://leetcode.com/problems/rotate-list/description/

Approach - using rotate array pattern 

Tc - n
Sc - 1
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0: return head
        if not head: return None
        
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        k = k % length
        if k == 0: return head
        curr = head
        curr = self.reverse(curr, None)
        first = curr
        
        while curr and k > 1:
            curr = curr.next
            k -= 1
        second = curr.next
        curr.next = None
        
        first = self.reverse(first, None)
        second = self.reverse(second, None)
        
        dummy = ListNode()
        dummy.next = first
        
        while first and first.next:
            first = first.next
        first.next = second
        
        return dummy.next
        
    def reverse(self, curr, prev):
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
"""
Optimal solution - Neetcode


tc- n
sc - 1
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        total = 0
        #find total nodes
        while curr:
            total += 1
            curr = curr.next
        
        #find effective K
        k = k % total
        if k == 0:
            return head
        
        #find pivot node
        curr = head
        temp = total - k
        while curr and temp > 1:
            curr = curr.next
            temp -= 1
        
        groupNext = curr.next
        curr.next = None
        
        #move second to last node and shift the pointers
        first = head
        second = groupNext
        while second.next:
            second = second.next
        second.next = first
        
        return groupNext
        
        