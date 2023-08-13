"""
https://leetcode.com/problems/copy-list-with-random-pointer/

Approach: first we need a dictionary. 
Whenever we are trying to clone something, we use dic.
first, while iterating through the linkedlist, we create a copy of the value and add it to the dic
Now, use another while to iterate over the linkedlist and add next and random pointers by indexing the dic


Tc: O(n) while loop
Tc: O(n) dictionary
"""
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None: None} #because random pointer may point to some None node
        original = head
        #first iteration we are just creating copies without any pointers
        #because random may point to any node and we may not have that node already created
        #so first create all nodes then assign pointers
        while original:
            copy = Node(original.val) #just node
            dic[original] = copy 
            original = original.next

        original = head
        #second iteration use the copy node we created and assign pointers
        while original:
            copy = dic[original]
            copy.next = dic[original.next]
            copy.random = dic[original.random]
            original = original.next

        return dic[head]
