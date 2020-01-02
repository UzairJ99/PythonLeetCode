class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        verticesP = []
        verticesQ = []

        if p:
            verticesP.append(p)
        if q:
            verticesQ.append(q)
        
        #initial case guards
        if verticesP == [] and verticesQ == []:
            return True
        elif len(verticesP) != len(verticesQ):
            return False
        elif verticesP[0].val != verticesQ[0].val:
            return False

        #DFS algorithm
        while len(verticesP) > 0:
            vertexP = verticesP.pop()
            vertexQ = verticesQ.pop()
            
            #check if both nodes exist and have equal value
            if (vertexP and vertexQ) and (vertexP.val == vertexQ.val):
                verticesP += [vertexP.left, vertexP.right]
                verticesQ += [vertexQ.left, vertexQ.right]
            #check if neither of the nodes exist
            elif (vertexP is None and vertexQ is None):
                continue
            else:
                return False
        
        return True