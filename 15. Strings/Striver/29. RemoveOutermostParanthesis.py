class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ""
        curr = ""
        
        for i in range(len(s)):
            char = s[i]
            if stack and char == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
            
            curr += char
            if not stack:
                res += curr[1:-1]
                curr = ""
        
        return res