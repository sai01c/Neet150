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
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))
            else:
                res.append("N")

        return ",".join(res) #array as a string 
    #["1", "2", "N"] to "12N"
    
    def deserialize(self, data):
        if data == "N": return #if input is just a null node we return []
        
        data = data.split(",") #string to array
        # "12N" to ["1", "2", "N"]
        q = collections.deque()
        root = TreeNode(data[0])
        q.append(root)
        i = 1 #we are starting at 1 because we already added root 
        while q: 
            node = q.popleft() #we pop always
            
            if i<len(data) and data[i] != "N": #we append only if not N
                node.left = TreeNode(data[i])
                q.append(node.left)
            i += 1 #we increment pointers always

            if i < len(data) and data[i] != "N": #i in in bounce
                node.right = TreeNode(data[i]) #creating a new node
                q.append(node.right) #adding that node to queue
            i += 1

        return root

