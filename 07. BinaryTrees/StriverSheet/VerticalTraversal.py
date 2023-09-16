"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
https://www.youtube.com/watch?v=xs_deEJXflw&ab_channel=SaiAnishMalla

Approach: 
idea is to visit every node and add to the dictionary
dictionary should look like this - {
                                    vertical : [(level, val), (level, val)], 
                                    vertical: [(level, value)]
                                    }

Now after completing the dictionary. 
Sort the dictionary based on vertical and then sort based on level

Tc: 
Sc: 

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        
        def helper(root, level, vertical):
            if not root:
                return
            dic[vertical].append((level, root.val))
            helper(root.left, level+1, vertical-1)
            helper(root.right, level+1, vertical+1)
        
        helper(root, 0, 0)
        res = []
        for vertical in sorted(dic.keys()):
            temp = []
            sortList = sorted(dic[vertical], key = lambda x: x[0])
            for level, val in sortList:
                temp.append(val)
            if temp:
                res.append(temp)
        return res
