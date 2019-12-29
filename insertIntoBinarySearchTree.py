class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        #check empty tree
        if root is None:
            root = TreeNode(val)
        else:
            #if node is less than value, insert on the right side
            if root.val < val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    #recurse through right side
                    self.insertIntoBST(root.right, val)
            #if node is greater than value, insert on the left side
            elif root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    #recurse through left side
                    self.insertIntoBST(root.left, val)
        #return final tree
        return root