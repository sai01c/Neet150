"""
https://leetcode.com/problems/binary-search-tree-iterator/

Approach - this is very straightforward. we do the inorder traversal and check if 
we have next node. to do this we can have a global pointer

tc
sc

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = self.inorder(root)
        self.k = -1
        
    def inorder(self, root):
        res = []
        if not root: return res
        res += self.inorder(root.left)
        res.append(root.val)
        res += self.inorder(root.right)
        return res

    def next(self) -> int:
        self.k += 1
        return self.nums[self.k]

    def hasNext(self) -> bool:
        if self.k + 1 < len(self.nums):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()