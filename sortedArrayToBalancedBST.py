class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if nums == []:
            return None
        
        mid = (len(nums))//2
        
        #make middle of array the root
        root = TreeNode(nums[mid])
        
        #append all left elements to the left of the root
        if len(nums[:mid]) > 0:
            #iterate recursively
            root.left = self.sortedArrayToBST(nums[:mid])
        else:
            #end of path
            root.left = None
        #append all right elements to the right of the root
        if len(nums[mid+1:])> 0:
            #iterate recursively
            root.right = self.sortedArrayToBST(nums[mid+1:])
        else:
            #end of path
            root.right = None
            
        return root