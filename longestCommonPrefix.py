class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short =strs[0]
        for s in strs:
            if len(s) < len(short):
                short = s
        res = ""
        for i in range(len(short)):
            temp =short[i] 
            for word in strs:
                if word[i] != temp:
                    return res
            else:
                res += temp
        return res
