"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Approach: we are going to use recurssion
if the node is Null, then obviously height is going to be zero
then apply same function left, right nodes
height is the maximum of the left and right. 

Tc: we will be visiting all the nodes so O(n)
Sc: since recurssion auxillary space will be O(n) if the tree is skewed

we can also use level order traversal to find the height/depth. This will also be 
Tc O(n) traverse every node 
Sc O(n) queue
"""


import collections


def depth(root):
    if root == None:
        # we are checking for height, so we return 0 if there's no node.
        return 0
    l = depth(root.left)
    r = depth(root.right)
    return (1 + max(l, r))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        q = collections.deque()
        q.append((root, 1))
        res = float('-inf')
        
        while q:
            for i in range(len(q)):
                node, ind = q.popleft()
                if node:
                    if not node.left and not node.right:
                        res = max(res, ind)
                        
                    q.append((node.left, ind+1))
                    q.append((node.right, ind+1))
        return res

