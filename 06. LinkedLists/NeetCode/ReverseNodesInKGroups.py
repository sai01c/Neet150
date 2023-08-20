"""
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Approach: we will find kth node each iteration and reverse linked list until this node
attach previous and next nodes. use groupPrev and groupNext pointers
read comments 

Tc - O(n), 
sc - O(1) 

"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(prev, k):
            while prev and k:
                k -= 1
                prev = prev.next
            if not k:
                return prev
            else:
                return False 
        def reverse(curr):
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        dummy = ListNode(0, head)
        tail = dummy
        prevGroup = tail
        curr = head
        
        while curr:
            kNode = getKth(prevGroup, k)
            if not kNode:
                return dummy.next
            nextGroup = kNode.next
            kNode.next = None

            prevGroup.next = reverse(curr)
            curr.next = nextGroup

            prevGroup = curr
            curr = nextGroup

        return dummy.next
        