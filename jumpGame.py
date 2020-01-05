class Solution:
    def canJump(self, nums):
        #index of current position
        pos = len(nums)-1
        
        for nextJump in range(len(nums)-1,-1,-1):
            #check if the next value added with it's index sums to the current index
            if nextJump + nums[nextJump] >= pos:
                #jump to that index
                pos = nextJump
        
        #check if you made it to the beginning of the array
        return pos == 0