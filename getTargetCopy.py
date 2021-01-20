# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def inOrder(original, cloned):
            if original:
                inOrder(original.left, cloned.left)
                if original is target:
                    self.result = cloned
                inOrder(original.right, cloned.right)
                
        inOrder(original, cloned)
        return self.result