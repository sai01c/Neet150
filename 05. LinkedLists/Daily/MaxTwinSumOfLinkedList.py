"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

Approach: list is even guaranteed. now go the middle of linked list and then
reverse the second half. Now add the first node from the first list and first node
from the reversed list

Tc: O(n)
Sc: O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        ans = 0
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        while fast and fast.next: #find middle of linked list
            slow = slow.next
            fast = fast.next.next
        second = slow.next 
        slow.next = None #close first half
        prev = None
        while second: #reverse second half
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first = head
        second = prev
        while first and second: #even list so both will exist
            temp = first.val + second.val
            ans = max(ans, temp)
            first = first.next #shift the pointer's to next node's
            second = second.next

        return ans
