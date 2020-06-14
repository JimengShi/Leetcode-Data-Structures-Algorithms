# Similar with problem 216
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        nums = [i for i in range(1, n+1)]
        
        def dfs(nums, path, begin, k):
            if len(path) == k:  
                output.append(path[:])
                return
            
            if len(path) > k:
                return
            
            for index in range(begin, len(nums)):
                path.append(nums[index])
                dfs(nums, path, index+1, k)
                path.pop()
        
        dfs(nums, [], 0, k)
        return output

# Time: O(k*N^k)=O(k*CNk) CNk is a number of combinations to build. append / pop operations are constant-time ones and the only consuming part here is to append the built combination of length k to the output.
# Space: O(N^k)=O(CNk) CNk is a number of combinations to build. So we need CNk to keep all the combinations for an output.