class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window approach
        maxSum = float('-inf')
        newSum = 0
        
        if (len(nums) == 1):
            return nums[0]
        if (len(nums) < 1):
            return None
        
        for num in nums:
            newSum += num
            maxSum = max(maxSum, newSum)
            newSum = max(newSum, 0)
                
        return maxSum
