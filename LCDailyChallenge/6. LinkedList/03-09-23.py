"""
https://leetcode.com/problems/linked-list-cycle-ii/

Approach: so one assumption is all node values are different. then it becomes easy
every time we add to visit set. if current node is in visit then we return the current node

Tc: O(n) Sc: O(n)
"""

def detectCycle(head):
    visit = set()
    curr = head
    while curr not in visit:
        if curr == None:
            return None
        visit.add(curr)
        curr = curr.next

    return curr
