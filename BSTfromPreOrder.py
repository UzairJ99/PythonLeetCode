class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        result = TreeNode(preorder[0])

        #iterate through list and append to BST
        for element in preorder:
            self.insert(result, element)

        return result
    
    def insert(self, root, x):
        #check empty tree
        if root is None:
            root = TreeNode(x)
        else:
            #if node is less than value, insert on the right side
            if root.val < x:
                if root.right is None:
                    root.right = TreeNode(x)
                else:
                    #recurse through right side
                    self.insert(root.right, x)
                    #if node is greater than value, insert on the left side
            elif root.val > x:
                if root.left is None:
                    root.left = TreeNode(x)
                else:
                    #recurse through left side
                    self.insert(root.left, x)