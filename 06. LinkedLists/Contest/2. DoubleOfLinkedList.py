"""
https://leetcode.com/contest/weekly-contest-358/problems/double-a-number-represented-as-a-linked-list/

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        carry = 0
        curr = prev
        ans = prev
        while curr:
            if curr:
                total = (curr.val*2)
            if carry:
                total += carry
            if curr:
                curr.val = total % 10
                curr = curr.next
            carry = total // 10
        prev = None
        curr = ans
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        if carry:
            node = ListNode(carry, prev)
            return node
        else:
            return prev