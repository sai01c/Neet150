"""
https://leetcode.com/problems/decode-string/

"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for i in range(len(s)):
            char = s[i]
            if char == "]":
                curr = ""
                while stack and stack[-1] != "[":
                    curr += stack.pop()
                stack.pop() #open brace
                fre = ""
                while stack and stack[-1].isnumeric():
                    fre += stack.pop()
                fre = int(fre[::-1])
                curr = curr[::-1]
                if stack:
                    stack += list(curr*fre)
                else:
                    res += (curr * fre) 
            else:
                stack.append(char)
        if not stack:
            return res
        else:
            return res + "".join(stack)
                