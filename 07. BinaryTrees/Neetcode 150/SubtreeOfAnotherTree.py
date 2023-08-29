"""
https://leetcode.com/problems/subtree-of-another-tree/

APPROACH: 
use the same tree function and apply it to s and t. 
if it satisfies with left or right, then it can be true

Tc: O(n) traverse every node once. 
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #No subroot then this is subtree
        if not subRoot: 
            return True    
        #No root then it is false because subroot can't be subtree of None    
        if not root: 
            return False
        #check for root and subroot
        if self.isSameTree(root, subRoot): 
            return True
        #check for children of root. if any of them satisfies then enough so OR.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p, q):
        #no root and subroot so True
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
        