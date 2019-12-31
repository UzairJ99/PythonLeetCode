class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1, root2):
        output = []

        #In-Order traversal (LNR)
        def traverseTree(root):
            if root:
                traverseTree(root.left)
                output.append(root.val)
                traverseTree(root.right)

        traverseTree(root1)
        traverseTree(root2)

        return sorted(output)