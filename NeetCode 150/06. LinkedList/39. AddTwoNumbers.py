"""
https://leetcode.com/problems/add-two-numbers/

reverse addition - do addition from left to right, you'll understand better

"""


def ListNode(self, val, next):
    self.val = val
    self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    if l1 or l2 or carry:  # edge case if carry is only left over
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry
        carry = val // 10  # quotient
        val = val % 10  # reminder
        curr.next = ListNode(val)

        curr = curr.next  # update pointer
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next
