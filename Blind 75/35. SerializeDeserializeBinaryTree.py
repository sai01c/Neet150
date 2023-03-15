"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Approach: this can be tricky but it is straight forward if you practice on paper

Serializing - we do level order traversal and if there is no node we just append "null"
most frustrating part is we need to return string and not array

Deserializing - we iterate over the input and use queue 

Tc: O(n)
Sc: O(n)

"""

import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        q = collections.deque()
        q.append(root)
        res = ""
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res += str(node.val)
            else:
                res += "N"

        return res
    
    def deserialize(self, data):
        if data == "N": return
        q = collections.deque()
        root = TreeNode(data[0])
        q.append(root)
        i = 1
        while q: 
            node = q.popleft() #we pop always
            if i<len(data) and data[i] != "N": #we append only if not N
                node.left = TreeNode(data[i])
                q.append(node.left)
            i += 1 #we increment pointers always

            if i < len(data) and data[i] != "N":
                node.right = TreeNode(data[i]) #creating a new node
                q.append(node.right) #adding that node to queue
            i += 1

        return root

