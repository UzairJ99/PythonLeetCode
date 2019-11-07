# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        #in order traversal: L N R
        #check empty
        if root is None:
            return None

        #iterate down to bottom left
        pointer = root
        while(pointer.left):
            print(pointer.left.val)
            pointer = pointer.left
        
        #new tree
        self.newNode = TreeNode(pointer.val)
        #store the head of the new tree
        pointer = self.newNode

        def traverseInOrder(root):
            if(root):
                #L
                traverseInOrder(root.left)
                #N
                print(root.val)
                #set the new node's right branch to the original trees value
                self.newNode.right = TreeNode(root.val)
                self.newNode = self.newNode.right
                #R
                traverseInOrder(root.right)
                
        traverseInOrder(root)
        
        #we return the right child to avoid duplicate roots
        return pointer.right