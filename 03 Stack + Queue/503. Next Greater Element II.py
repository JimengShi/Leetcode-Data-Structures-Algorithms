class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # (1) initialize data structure
        stack = []
        res = [-1] * len(nums)
        
        # (2) traverse the new nums = nums + nums
        newnums = nums + nums
        for i in range(len(newnums)):
            while stack and newnums[stack[-1]] < newnums[i]:
                v = stack.pop()
                if v >= 0 and v < len(nums):
                    res[v] = newnums[i]
            stack.append(i)
            
        # (3) return result
        return res

# Time: O(N)
# Space: O(N)
    
    
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:    
        stack, r = [], [-1] * len(nums)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                r[stack.pop()] = nums[i]
            stack.append(i)
        print(r)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                r[stack.pop()] = nums[i]
            if stack == []:
                break
        return r
    
# Time: O(N)
# Space: O(N)