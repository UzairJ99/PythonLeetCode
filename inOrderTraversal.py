class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        output = []
        
        def traversal(root):
            if root is not None:
                #recursively iterate through left nodes
                if root.left is not None:
                    traversal(root.left)
                #append current node
                output.append(root.val)
                #recursively iterate through right nodes
                if root.right is not None:
                    traversal(root.right)
        #call traversal method
        traversal(root)
        return output