"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Approach: this is basically level order traversal.
Only change is while appending level each iteration reverse the array using flag

TC: O(n)
Sc: O(n)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []
        reverse = False
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if level and reverse == False:
                res.append(level)
                reverse = True
            elif level and reverse == True:
                res.append(self.reverse(level, 0, len(level) - 1))
                reverse = False
        return res
    
    def reverse(self, arr, left, right):
        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
        return arr
        