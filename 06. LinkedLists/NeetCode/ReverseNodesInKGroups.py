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

TODO
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k) #get Kth node
            if not kth: #if there's no k then we can end the loop
                break
            groupNext = kth.next #next group
            
            #reverse linked list
            prev = groupNext #notice how we are taking next group as prev. 
            # we are directly joining this group to next group
            curr = groupPrev.next #reverse current group
            while curr != groupNext: 
            #as we want to reverse only this group you can compare curr to next group
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            #update groupPrev 
            #write on paper to understand this
            temp = groupPrev.next 
            groupPrev.next = kth #attach prev group to reversed current group
            groupPrev = temp
            
        return dummy.next
            
        
    def getKth(self, curr, k): #get kth node
        while curr and k > 0:
            curr = curr.next
            k -= 1
            
        return curr