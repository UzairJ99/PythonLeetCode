class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        #check empty tree
        if len(nums) < 1:
            return None
        
        #recursively create a maximum binary tree
        def maxTree(nums):
            #get index of largest element in list
            ix = nums.index(max(nums))
            #construct a node using that element
            node = TreeNode(nums[ix])
            
            #recursively create the right side of the tree
            if len(nums[ix+1:]) > 0:
                node.right = maxTree(nums[ix+1:])
            #recursively create the left side of the tree
            if len(nums[:ix]) > 0:
                node.left = maxTree(nums[:ix])
                
            return node
        
        return maxTree(nums)