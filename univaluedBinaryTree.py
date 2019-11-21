class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        
        value = root.val
        self.check = True
        
        def traversal(root):
            if root:
                traversal(root.left)
                #check if at any time the value is different from the root value
                if value != root.val:
                    self.check = False
                traversal(root.right)
                
        traversal(root)
                
        return self.check