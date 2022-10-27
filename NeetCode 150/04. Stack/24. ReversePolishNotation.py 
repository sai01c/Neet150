"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Approach: this is a straight forward question. Iterate over the stack and perform operations

there is one learning from this problem - 

10/3 = 3.33
10//3 = 3

but, for negative numbers - 
-10/3 = -3.33
-10//3 = -4 (floor division means take least number)

Sc: O(n) for stack
Tc: O(n) iterating once
"""


def evalRPN(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))  #we can't do floor division here as numbers can also be negative
        else:
            stack.append(int(c))
    return stack[0]
