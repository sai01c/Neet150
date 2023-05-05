"""
https://leetcode.com/problems/add-two-numbers/

Approach: reverse addition - do addition from left to right, you'll understand better.
if sum is 10, node will be 0 and 1 will carry to next iteration.

Tc: O(max(l1, l2))
Sc: O(1)

"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry: #lengths of them may be diff
            #carry might be left over also
            total = 0 #initate total to zero for this iteration
            if l1:
                total += l1.val
                l1 = l1.next #shift the pointers
            if l2:
                total += l2.val
                l2 = l2.next
            if carry:
                total += carry
                
            carry = total // 10 #example 15 - node is 5 carry is 1
            digit = total % 10

            node = ListNode(digit) #create a node with that digit
            tail.next = node
            tail = tail.next
            
        return dummy.next
            
            
        