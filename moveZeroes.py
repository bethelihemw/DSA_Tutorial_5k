def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seek = 0
        hold = 0
        while seek < len(nums):
            if nums[seek] != 0:
                nums[seek],nums[hold] = nums[hold],nums[seek]
                hold = hold +1

            seek = seek +1
        return nums
