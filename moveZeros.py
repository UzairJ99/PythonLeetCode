class Solution:
    def moveZeroes(self, nums):
        #set pointers for the current element and the last nonzero number encountered
        curr = 0
        nonzero = 0
        
        #edge case
        if nums == []:
            return None
        
        #skip to the first zero
        while nums[curr] != 0 and curr < len(nums)-1:
            curr += 1
            nonzero += 1

        #swap each zero with the next nonzero value
        for nonzero in range(nonzero, len(nums)):
            if nums[curr] == 0 and nums[nonzero] != 0:
                nums[curr], nums[nonzero] = nums[nonzero], nums[curr]
                curr += 1