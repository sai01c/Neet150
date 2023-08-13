"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

Approach - have a dic and copy the first linked list to dic
now while iterating second linked list if the node is already present in dic return that node

tc - m + n
sc - m we are storing m nodes in dic

"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first = headA
        dic1 = defaultdict(int)
        second = headB
        while first:
            dic1[first] += 1
            first = first.next
            
        while second:
            if second in dic1:
                return second
            second = second.next
        