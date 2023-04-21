class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        res = 0
        prev = 0
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            val = dic[char]

            if val < prev:
                res -= val
            else:
                res += val
            
            prev = val
        
        return res