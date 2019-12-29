class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        #check empty tree
        if root is None:
            return None
        
        levelCount = 1 #level tracker
        averages = [root.val] #output
        vertices = [root] #queue

        while len(vertices) > 0:
            #breadth-first search algorithm
            vertex = vertices.pop(0)
            levelCount -= 1

            if vertex.left is not None:
                vertices.append(vertex.left)
            if vertex.right is not None:
                vertices.append(vertex.right)
            #check if level has been completed
            if levelCount == 0:
                levelCount = len(vertices)
                #calculate the average of the level and add it to the list
                if len(vertices) > 0:
                    #sum all the values for each node in the queue
                    avg = sum([x.val for x in vertices])/len(vertices)
                    averages.append(avg)
        
        return averages