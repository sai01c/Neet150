"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

Approach - 
first go to the first node
from here try to reach end node. maitain two pointers one from head and one from first
one will reach the end other will stop at the kth node from end. 

tc - n
sc - 1
"""

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        for i in range(k-1):
            first = first.next
        last = head
        fast = first
        while fast and fast.next:
            fast = fast.next
            last = last.next
        
        first.val, last.val = last.val, first.val
        return head
        
        