class Solution:
    def findUnion(self, a, b):
        sums = a+b
        result = set(sums)
        return len(result)
