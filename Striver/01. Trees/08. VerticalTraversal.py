"""
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


def verticalTraversal(root):
    vertical = 0
    level = 0
    dic = {}
    helper(root, vertical, level, dic)
    res = []
    for vertical in sorted(dic.keys()):
        column = []
        for level, val in sorted(dic[vertical]):
            column.append(val)
        res.append(column)
    return res


def helper(root, vertical, level, dic):
    if vertical not in dic:
        dic[vertical] = [(level, dic)]
    else:
        dic[vertical].append([(level, dic)])

    helper(root.left, vertical - 1, level + 1, dic)
    helper(root.right, vertical + 1, level + 1, dic)
