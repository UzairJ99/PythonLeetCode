class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        vertices = [root]
        #list to return
        nodes = []
        #keep track of what element we're at in the level
        levelCount = 1
        depth = 0
        
        #check empty tree
        if root is None:
            return None

        while len(vertices) > 0:
            vertex = vertices.pop(0)
            #if the depth is not an index in the 2D list, create an empty list and append vertex to it
            if depth == len(nodes):
                nodes.append([vertex.val])
            else:
                #add the vertex to the list of values at the current depth
                nodes[depth].append(vertex.val)

            levelCount -= 1

            if vertex.left:
                vertices.append(vertex.left)
            if vertex.right:
                vertices.append(vertex.right)
            
            #check if a level has been completed
            if levelCount == 0:
                levelCount = len(vertices)
                #incrementing depth allows us to increment to the next index of the 2D list
                depth += 1
        
        return nodes

            