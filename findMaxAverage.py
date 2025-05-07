def findMaxAverage(self, nums: List[int], k: int) -> float:
        win =nums[0:k]
        curr = sum(win)
        maxs = [curr]
        for i in range(k,len(nums)):
            curr= curr- nums[i - k] + nums[i]
            maxs.append(curr)
        maxi = max(maxs)
        return maxi/k
