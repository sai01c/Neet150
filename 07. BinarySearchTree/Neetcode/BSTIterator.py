"""
https://leetcode.com/problems/binary-search-tree-iterator/

Approach - this is very straightforward. we do the inorder traversal and check if 
we have next node. to do this we can have a global pointer

tc
sc

"""

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = -1
        self.res = []
        self.inorder(root)
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
        

    def next(self) -> int:
        self.curr += 1
        return self.res[self.curr]

    def hasNext(self) -> bool:
        if self.curr + 1 < len(self.res):
            return True
        else:
            return False
