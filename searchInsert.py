class Solution:
    def searchInsert(self, nums, target):
        if len(nums) < 2:
            if target <= nums[0]:
                return 0
            else:
                return 1
        else:
            for x in range(len(nums) - 1):
                if nums[x] > target or nums[x] == target:
                    return x
                elif nums[x] < target and nums[x+1] >= target:
                    return x + 1
                elif nums[-1] < target:
                    return len(nums)