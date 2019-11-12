class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        lvs = self.depthFirstSearch(root1)
        lvs2 = self.depthFirstSearch(root2)
        return lvs == lvs2

    def depthFirstSearch(root):
        stack = [root]
        visited = []
        #holds the leaf values from left to right
        leaves = []

        while len(stack) > 0:
            vertex = stack.pop()
            if vertex not in visited:
                #check if it's a leaf
                if vertex.right is None and vertex.left is None:
                    leaves.append(vertex.val)
                    continue
                #push right leaf to stack first so that left is popped before right
                if vertex.right:
                    stack.append(vertex.left)
                if vertex.left:
                    stack.append(vertex.right)
        
        return leaves