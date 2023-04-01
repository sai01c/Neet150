"""
https://leetcode.com/problems/find-duplicate-subtrees/

Approach: use dfs function and we create a dict with key as Node.val strings and values as TreeNodes
check if the length if is more than 1 then duplicate tree exists.


"""

def duplicate(root):
    count = defaultdict(list) 
    res = []

    def dfs(node):
        if not node:
            return "null"
        s = ",".join([str(node.val), dfs(node.left), dfs(node.right)]) #this part of logic is tough
        if len(count[s]) == 1: 
            res.append(node)
        count[s].append(node)
        return s
    
    dfs(root)
    return res