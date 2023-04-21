


class Solution:
    def beautySum(self, s: str) -> int:

        res = 0
        for i in range(len(s)):
            dic = defaultdict(int)
            sub = ""
            for j in range(i, len(s)):
                sub += s[j]
                dic[s[j]] += 1

                if len(dic) > 1:
                    
                    maxi = max(dic.values())
                    mini = min(dic.values())
                    res += (maxi-mini)
        
        return res
