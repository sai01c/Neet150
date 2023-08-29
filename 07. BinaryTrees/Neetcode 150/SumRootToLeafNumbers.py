"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/

Approach: we are going to do bfs solution. wherever bfs is possible do bfs instead of dfs
Now, to the queue each time we'll add node + path value.
we can get path value by multiplying prev val by 10 and adding current val
if there is no left and no right then it is leaf node, we add this sum to our res.

Tc: O(n) bfs
Sc: O(n) queue

"""

def sumNumbers(root):
    res = 0
    q = collections.deque()
    q.append((root, root.val))

    while q:
        node, pathSum = q.popleft()
        if node.left:
            q.append((node.left, pathSum*10 + node.left.val))
        if node.right:
            q.append((node.right, pathSum*10 + node.right.val))
        if (not node.left and not node.right):
            res += pathSum
    
    return res
