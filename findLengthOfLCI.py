class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if nums == []: 
            return 0
        
        greatestSize = 1
        size = 1
        output = [nums[0]]
        # loop through list
        for elem in range(1,len(nums)):
            # add to output list if curr is greater than prev
            if nums[elem] > nums[elem-1]:
                output.append(nums[elem])
                size = len(output)
            else:
                # reset output list if not
                size = 1
                output = [nums[elem]]
            # save size if larger than prev size
            if (size > greatestSize):
                greatestSize = size
        
        # return largest size
        return greatestSize