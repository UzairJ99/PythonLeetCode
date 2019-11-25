class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root):
        nodes = [root]
        visited = []
        number = ""
        output = 0

        while len(nodes)>0:
            node = nodes.pop()
            #append digit to number
            number += (str(node.val))
            if node not in visited:
                #check if right node has not been visited before
                if node.right and node.right not in visited:
                    nodes.append(node.right)
                #check if left node has not been visited before
                if node.left and node.left not in visited:
                    nodes.append(node.left)
                #check if all children have been visited
                if (node.right in visited and node.left in visited) or (node.right is None and node.left in visited) or (node.left is None and node.right in visited):
                    visited.append(node)
                    #reset the DFS to begin from the root
                    nodes = [root]
                    number = ""
                #check if end of path has been reached
                if node.right is None and node.left is None:
                    visited.append(node)
                    #reset the DFS now that we've completed a path
                    nodes = [root]
                    number = int(number, 2) #convert to decimal
                    output += number #add to sum
                    number = "" #reset number for the next path
                    
                    
        return output