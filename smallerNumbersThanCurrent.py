def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            counts = 0
            for j in range(len(nums)):
                if i > nums[j]:
                    counts = counts + 1
            result.append(counts)
        return result
