class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        vertices = [root]
        levelCount = 1;
        depth = 0;

        #check empty tree
        if root is None:
            return 0;

        #BFS algorithm
        while (len(vertices)>0):
            #pop from queue
            vertex = vertices.pop(0)
            levelCount -= 1;
            #check for children
            if (vertex.left):
                vertices.append(vertex.left)
            if (vertex.right):
                vertices.append(vertex.right)
            #check if all nodes of the level have been popped
            if (levelCount == 0):
                depth += 1
                #reset levelCount to the number of nodes in the next level of the tree
                levelCount = len(vertices)

        return depth