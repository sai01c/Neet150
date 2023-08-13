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
        

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = 0, 0
        curr = headA
        while curr:
            l1 += 1 #find total nodes in A
            curr = curr.next
        curr = headB
        while curr:
            l2 += 1 #find total nodes in B
            curr = curr.next
        
        if l1 > l2:
            curr = headA
            while l1 != l2:
                curr = curr.next
                l1 -= 1
            a = curr #start both at same length
            b = headB
        elif l1 < l2:
            curr = headB
            while l1 != l2:
                curr = curr.next
                l2 -= 1
            a = headA
            b = curr
        else:
            a = headA
            b = headB
        while a and b: #check if they are equal
            if a == b:
                return a
            a = a.next
            b = b.next
        return None
        