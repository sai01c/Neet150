"""
https://leetcode.com/problems/reverse-nodes-in-k-group/

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