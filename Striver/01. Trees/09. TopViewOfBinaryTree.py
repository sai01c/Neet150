"""
https://www.youtube.com/watch?v=xs_deEJXflw&ab_channel=SaiAnishMalla

Approach: 
idea is to visit every node and add to the dictionary
dictionary should look like this - {
                                    vertical : [(level, val), (level, val)], 
                                    vertical: [(level, value)]
                                    }

Now after completing the dictionary. 
Sort the dictionary based on vertical and then sort based on level. 

Return the first element of the column as we want the top view

Tc: 
Sc: 

"""


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        self.helper(root, 0, 0, dic)
        res = []

        for vertical in sorted(dic.keys()):
            column = []
            for level, val in sorted(dic[vertical]):
                column.append(val)
            res.append(column[0])
        return res

    def helper(self, root, vertical, level, dic):
        if not root:
            return
        #{vertical: (level, root.val)}
        if vertical in dic:
            dic[vertical].append((level, root.val))
        else:
            dic[vertical] = [(level, root.val)]
        self.helper(root.left, vertical - 1, level + 1, dic)
        self.helper(root.right, vertical + 1, level + 1, dic)
