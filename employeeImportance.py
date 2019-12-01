class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        #get the root employee
        root = self.getEmployee(employees, id)
        #push to stack
        visited = [employees[root]]
        importance = 0

        #Depth First Search Algorithm
        while len(visited) > 0:
            employee = visited.pop()
            importance += employee.importance
            for subordinate in employee.subordinates:
                visited.append(employees[self.getEmployee(employees,subordinate)])
        
        return importance

    def getEmployee(self, employees, id):
        #search for employee by their ID
        for index, employee in enumerate(employees):
            if employee.id == id:
                return index
        #not found
        return -1