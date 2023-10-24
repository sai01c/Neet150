
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: ListNode, target: int):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            if prev.val == target:
                head.next = curr
                return prev

obj = Solution()       
result = obj.reverse(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)

print(result)