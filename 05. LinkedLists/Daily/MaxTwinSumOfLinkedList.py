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

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Approach: we need to modify the array in place. sliding window concept but with diff logic. w
we inititate right at 0 and check if right == right + 1. out of the min of 2, count 
we append the right to the left index and increase left index.
end return left index as this will have the length of the new array

Tc: 
Sc: 
this problem is similar to string compression
"""

def removeDuplciates(nums):
    left = 0
    right = 0
    while right < len(nums):
        count += 1
        while right +  1 < len(nums) and nums[right] == nums[right+1]:
            count += 1
            right += 1
        for i in range(min(2, count)):
            nums[left] = nums[right]
            left += 1
        right += 1
    return left

