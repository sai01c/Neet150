"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

APPROACH: 

We use the same height function. But make couple of modifications
- Here path sum will be the node.val plus max of left and right. 
- we also use a maximum value to which we keep adding the left, right, root and check for max value
- we also use to check left and right are more than 0 because we might have negative values

Tc: O(n) traverse every node once. 
Sc: O(n) recursion stack
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.height(root)
        return self.res

    def height(self, root):
        if not root:
            return 0
        leftH = max(0, self.height(root.left))
        rightH = max(0, self.height(root.right))
        #left and right we are taking max of 0 and height because imagine this example -
        # [2,-1] ideally we should return 2

        self.res = max(self.res, leftH + rightH + root.val) #this is tricky part - draw on 
        #paper to understand this more

        return root.val + max(leftH, rightH)
