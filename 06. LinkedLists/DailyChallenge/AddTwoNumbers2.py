"""
https://leetcode.com/problems/add-two-numbers-ii/

approach - reverse linked lists and do add two numbers

tc - n
sc - 1

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = self.reverse(l1, None)
        second = self.reverse(l2, None)
        
        dummy2 = ListNode()
        tail = dummy2
        carry = 0

        while first or second or carry:
            total = 0
            if first:
                total += first.val
                first = first.next
            if second:
                total += second.val
                second = second.next
            total += carry
            digit = total % 10
            carry = total // 10
            node = ListNode(digit)
            tail.next = node
            tail = tail.next
        return self.reverse(dummy2.next, None)
        
        
        
    def reverse(self, curr, prev):
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        curr = l1
        while curr:
            s1.append(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            s2.append(curr.val)
            curr = curr.next
        dummy = ListNode()
        prev = dummy
        carry = 0
        while s1 or s2 or carry:
            total = 0
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            if carry:
                total += carry
            carry = total // 10
            total = total % 10
            prev.next = ListNode(total)
            prev = prev.next
        
        def helper(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        return helper(dummy.next)
            

            