class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def bstToGst(self, root):
        #keep track of sum of original BST
        self.sum = 0
        #traverse through BST in reverse order to sum up values
        def reverseOrderTraversal(root):
            if root:
                reverseOrderTraversal(root.right)
                #add the root value to the sum
                self.sum += root.val
                #set the root value to the accumulated sum
                root.val = self.sum
                reverseOrderTraversal(root.left)
                
        reverseOrderTraversal(root)
        #return modified tree
        return root
    