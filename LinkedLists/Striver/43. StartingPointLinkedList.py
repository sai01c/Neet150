"""
https://leetcode.com/problems/linked-list-cycle-ii/

Approach - use set to find duplicate if node is in the set then this is the starting point

tc - n
sc - n

"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visit = set()
        curr = head
        while curr not in visit:
            if curr == None: 
                return None
            visit.add(curr)
            curr = curr.next
        return curr