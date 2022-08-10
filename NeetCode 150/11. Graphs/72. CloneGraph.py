"""
https://leetcode.com/problems/clone-graph/

Approach: we'll use a dictionary to store the copy of the node.
then, use a for loop to iterate over the neighbors of the original node
and append the same recurring function to the copy we created

TC: O(n) as we are iterating only once
Sc: O(n) as we are using dictionary
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def graphClone(self, node: 'Node') -> 'Node':
        dic = {}

        def clone(node):
            if node in dic:  # if node is there is the dic
                return dic[node]
            copy = Node(node.val)  # create a copy
            dic[node] = copy  # add copy to dict
            for nei in node.neighbors:
                # for all the neighbors of the original node
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None


obj = Solution()
print(obj.graphClone([[2, 4], [1, 3], [2, 4], [1, 3]]))
