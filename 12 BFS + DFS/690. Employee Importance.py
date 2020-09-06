# You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. 
# They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], 
# and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

# Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

# Example 1:
# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# Output: 11

# Explanation:
# Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. 
# They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.


# Employee info
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: List[int]):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates

# Method 1: DFS recursion    
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # (1) table = { 1:[1,5,[2,3]], 2:[2,3,[]], 3:[3,3,[]] }
        table = {emp.id: emp for emp in employees}  
        
        # (2) dfs
        def dfs(emp):                           # emp is a certain object: [1, 5, [2, 3]]
            # if emp.subordinates == []:          # base case
            #     return emp.importance

            value = emp.importance
            for sub in emp.subordinates:        # subordinates for employee
                if sub:
                    value += dfs(table[sub])
            return value

        # (3) call dfs
        return dfs(table[id])

# Time: O(N), where N is the number of employees. We might query each employee in dfs.
# Space: O(N), the size of the implicit call stack when evaluating dfs.  


# Method 2: DFS with stack  
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # (1) initialize
        value = 0
        
        # (2) save employee in a dictionary
        table = {}
        for emp in employees:
            table[emp.id] = emp

        # (3) dfs
        stack = [table[id]]
        while stack:
            emp = stack.pop()
            value += emp.importance
            
            for sub in emp.subordinates:
                if sub:
                    stack.append(table[sub])
            
        # (4) return result
        return value

# Time: O(N), where N is the number of employees. We might query each employee in dfs.
# Space: O(N), the size of the implicit call stack when evaluating dfs. 


# call method:
# e1 = 
# e2 = 
# e3 =
# employees = [e1, e2, e3]

# if __name__ == "__main__":
#     id = 1
#     employees = [e1, e2, e3]
#     print(Solution().getImportance(employees, id)