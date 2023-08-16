"""
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



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
