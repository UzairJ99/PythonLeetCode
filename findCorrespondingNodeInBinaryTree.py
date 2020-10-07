# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        
        if not original or not cloned:
            return None
        
        treeStack = [(original, cloned)]  # use a stack to traverse through the tree
        
        while treeStack:
            org, copy = treeStack.pop()
            
            if org == target:
                return copy  # return the matching node in the cloned tree
            
            # traverse the rest of the tree
            if org.left:
                treeStack.append((org.left, copy.left))
            if org.right:
                treeStack.append((org.right, copy.right))
        