"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/


"""

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        if len(preorder) == 1:
            return node
        
        left = preorder[1]
        leftSize = postorder.index(left) + 1
        
        node.left = self.constructFromPrePost(preorder[1:leftSize+1], postorder[:leftSize])
        node.right = self.constructFromPrePost(preorder[leftSize+1:], postorder[leftSize:-1])
        
        return node
    

    0 or 0 is 0