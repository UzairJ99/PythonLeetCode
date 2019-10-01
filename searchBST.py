# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        def traverseTree(root):
            if root:
                if root.val == val:
                    #assigns the found root as the subtree
                    self.subTree = root
                if root.val > val:
                    traverseTree(root.left)
                if root.val < val:
                    traverseTree(root.right)
            else:
                #if the value is not found the subtree should be assigned null
                self.subTree = None
        
        self.subTree = TreeNode(None)
        traverseTree(root)
        return self.subTree