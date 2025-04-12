class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,i+2):
                if nums[i]== nums[j]:
                    nums[i] = nums[i]*2
                    nums[j] = 0
        print(nums)
        for k in range(len(nums)):
            if nums[k] == 0:
                nums.append(nums[k])
                nums.remove(nums[k])
        return nums
