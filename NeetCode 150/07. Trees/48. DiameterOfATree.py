"""
https://leetcode.com/problems/diameter-of-binary-tree/

Approach - Key here is that for any node diameter is the sum of left height and right height

Tc: O(n) traverse every node 
Sc: O(n) auxillary space
"""


def brute_diameter(root):
    if root == None:
        return 0
    ans = 0
    lh = height(root.left)
    rh = height(root.right)
    ans = max(ans, lh + rh) #then find the diameter by adding them 
    brute_diameter(root.left) #now, repeat for all the left and right nodes
    brute_diameter(root.right)
    return ans

#this will be O(n^2) because every time you are using height function already inside diamter function
#practice tree problems on paper. 


def brute_height(root): #find the height of left and right node using regular approach
    if root == None: 
        return 0
    l = height(root.left)
    r = height(root.right)
    return 1 + max(l, r)


def diameter(root):
    ans = 0
    height(root)
    return ans


def height(root):
    if root == None:
        return 0
    l = height(root.left) #find height of left and right nodes
    r = height(root.right)
    # key is to add diamter formula inside height formula
    #there itself find the max of left and right by using some global variable
    ans = max(ans, l + r)
    return 1 + max(l, r)
