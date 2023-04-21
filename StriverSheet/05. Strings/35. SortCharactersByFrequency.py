class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        sortList = sorted(dic.items(), key = lambda x:x[1], reverse = True)

        res = ""
        for char, fre in sortList:
            while fre > 0:
                res += char
                fre -= 1
        return res
        