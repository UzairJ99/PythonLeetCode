class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums)-1  #end bounds
        mid = (lo+hi)//2
        
        while (lo <= hi):
            mid = (lo+hi)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                #elminate left half including mid
                lo = mid + 1
            else:
                #eliminate right half including mid
                hi = mid - 1
        
        #not found
        return -1