class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        if root:
            levelCount = 1
        else:
            levelCount = 0
            return None
        
        averages = [root.val]
        visited = []
        vertices = [root]
        values = [root.val]

        while len(vertices) > 0:
            #breadth-first search algorithm
            vertex = vertices.pop(0)
            value = values.pop(0)
            levelCount -= 1

            if vertex not in visited:
                visited.append(vertex)
                if vertex.left is not None:
                    vertices.append(vertex.left)
                    values.append(vertex.left.val)
                if vertex.right is not None:
                    vertices.append(vertex.right)
                    values.append(vertex.right.val)
                #check if level has been completed
                if levelCount == 0:
                    levelCount = len(vertices)
                    #calculate the average of the level and add it to the list
                    avg = sum(values)/len(values)
                    averages.append(avg)
        
        return averages
