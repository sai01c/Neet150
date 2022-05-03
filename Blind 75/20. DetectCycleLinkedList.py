"""
https://leetcode.com/problems/linked-list-cycle/

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Approach: we shall two pointers slow and fast. 
slow moves by one node and fast moves by two nodes. 
if there is a cycle at one point both will be equal. 

TC: O(n) iterating once
SC: O(n) copying linked list twice
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False


s = Solution()
print(s.hasCycle([3, 2, 0, -4]))
