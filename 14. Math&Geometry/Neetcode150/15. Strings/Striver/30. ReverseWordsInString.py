class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        r = 0
        words = []
        while r < len(s):
            if s[r] != " ":
                r += 1
            else:
                word = (s[l:r])
                if len(word) > 0: words.append(word)
                r += 1
                l = r
        
        word = (s[l:r])
        if len(word) > 0: words.append(word)
        
        l = 0
        r = len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1

        res = ""
        for w in words:
            res += w
            res += " "
        return res[:-1]