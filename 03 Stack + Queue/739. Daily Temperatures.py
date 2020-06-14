class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                ans[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
            
        return ans
    
# Time: O(N), where N is the length of T. Each index gets pushed and popped at most once from the stack.
# Space: O(N).

    
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: 
            return []

        result = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack:
                prev = stack[-1]
                if T[prev] < T[i]:
                    result[prev] = i - prev
                    stack.pop()
                else:
                    break
            stack.append(i)
            
        return result
    
# Time: O(N), where N is the length of T. Each index gets pushed and popped at most once from the stack.
# Space: O(N).