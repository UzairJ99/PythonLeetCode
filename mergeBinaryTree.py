# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def traverseTree(self, root1, root2, root3):
        #if neither are None
        if root1 is not None and root2 is not None:
            #combine values
            root3 = TreeNode(root1.val + root2.val)
            #traverse through tree 1, 2 and the new tree simultaneously
            root3.left = root3.traverseTree(root1.left, root2.left, root3.left)
            root3.right = root3.traverseTree(root1.right, root2.right, root3.right)
        elif root1 is not None and root2 is None:
            root3 = TreeNode(root1.val)
            root2 = TreeNode(None)
            root3.left = root3.traverseTree(root1.left, root2.left, root3.left)
            root3.right = root3.traverseTree(root1.right, root2.right, root3.right)
        elif root1 is None and root2 is not None:
            root3 = TreeNode(root2.val)
            root1 = TreeNode(None)
            root3.left = root3.traverseTree(root1.left, root2.left, root3.left)
            root3.right = root3.traverseTree(root1.right, root2.right, root3.right)
        
        return root3

class Solution:
    def mergeTrees(self, t1, t2):
        t3 = TreeNode(None)
        t3 = t3.traverseTree(t1,t2,t3)
        if t3.val is None:
            return None
        else:
            return t3