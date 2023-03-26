"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

APPROACH: inorder traversal and get the elements in ascending order then find the kth element

Tc: O(n) traverse every node once
Sc: O(n) using array here
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self.inOrder(root)
        return self.res[k-1] #we need the kth element. This is O(n) 
         
    #inorder traversal of BST will be sorted array
    def inOrder(self, root): 
        if not root: return None
        self.inOrder(root.left) #left first
        self.res.append(root.val) #append root value
        self.inOrder(root.right) #right last
