# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        #search binary search tree
        def traverseTree(node):
            #check if not None
            if node:
                #check if node is in range
                if L <= node.val <= R:
                    #add to sum
                    self.sum += node.val
                #if the node value is greater than the left bound we recurse left
                if node.val > L:
                    traverseTree(node.left)
                if node.val < R:
                    traverseTree(node.right)
        
        self.sum = 0
        #traverse through tree
        traverseTree(root)
        return self.sum