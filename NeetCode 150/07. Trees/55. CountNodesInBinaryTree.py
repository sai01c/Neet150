"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

APPROACH: 
Have a helper function where you pass the nodea and the maxValue so far. 
if the node.val is greater than maxValue , we increase the output by 1
repeat for left and right nodes. 

O(n) traverse every node once
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0
        return self.helper(root, root.val) #initiate root value as maxi
        
    def helper(self, root, maxvalue):
        if not root: #base case - no root 
            return 0
        #if root value is greater than path maxi then we found new maxi
        if root.val >= maxvalue: 
            self.output += 1
            maxvalue = max(root.val, maxvalue)
            
        self.helper(root.left, maxvalue) #dfs on left and right nodes
        self.helper(root.right, maxvalue)
        
        return self.output