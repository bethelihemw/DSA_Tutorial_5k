class Solution:
    def similarPairs(self, words: List[str]) -> int:
        result = []
        for i in words:
            result.append(set(i))
        maxs = []
        count = 0
        for j in range(len(result)):
            for k in range(j+1, len(result)):
                if result[j] == result[k]:
                    count = count + 1
            maxs.append(count)
        return max(maxs)
