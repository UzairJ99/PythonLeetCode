# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    #depth-first search algorithm
    def maxDepth(self, root):
        visited = []
        vertices = [root]
        depth = 0
        #check for empty graph
        if root:
            levelCount = 1
        else:
            levelCount = 0
            return 0

        #breadth-first search algorithm
        while len(vertices) > 0:
            vertex = vertices.pop(0) #pop first item in queue
            levelCount -= 1 #subtract an element from the level count

            if vertex not in visited:
                visited.append(vertex)
                if len(vertex.children) > 0:
                    #push child nodes onto the queue
                    vertices += vertex.children
                #if there are no more elements on the level, we've completed a new depth
                if levelCount == 0:
                    #set to the number of elements left in the queue, which is also the number of elements in the next level
                    levelCount = len(vertices)
                    depth += 1
        
        return depth