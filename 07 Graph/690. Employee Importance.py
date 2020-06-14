# Employee info
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: List[int]):
#         self.id = id                      # It's the unique id of each node. unique id of this employee     
#         self.importance = importance      # the importance value of this employee
#         self.subordinates = subordinates  # the id of direct subordinates

# Method 1: DFS recursion    
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = {emp.id: emp for emp in employees}
        
        def dfs(emp):                           # emp is a certain object: [1, 5, [2, 3]]
            if emp.subordinates == []:          # base case
                return emp.importance

            value = emp.importance
            for sub in emp.subordinates:        # subordinates for employee
                value += dfs(table[sub])
            return value

        return dfs(table[id])

# Time: O(N), where N is the number of employees. We might query each employee in dfs.
# Space: O(N), the size of the implicit call stack when evaluating dfs.  


# Method 2: DFS with stack  
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        value = 0
        table = {}
        for emp in employees:
            table[emp.id] = emp

        stack = [table[id]]
        while stack:
            emp = stack.pop()
            for sub in emp.subordinates:
                stack.append(table[sub])
            value += emp.importance

        return value

# Time: O(N), where N is the number of employees. We might query each employee in dfs.
# Space: O(N), the size of the implicit call stack when evaluating dfs.  