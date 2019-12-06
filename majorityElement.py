class Solution:
    def majorityElement(self, nums):
        countDict = {}
        
        #edge cases
        if nums == []:
            return 0
        
        if len(nums) < 2:
            return nums[0]
        
        #count each element
        for x in nums:
            if countDict.get(x):
                countDict[x] += 1
                #check if it is the majority element
                if countDict[x] > len(nums)//2:
                    return x
            else:
                countDict[x] = 1