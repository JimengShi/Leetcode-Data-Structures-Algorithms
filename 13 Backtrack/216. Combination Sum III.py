# Method 1: sorting and pruning more
class Solution(object):
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        res = []
        path = []
        self.dfs(candidates, k, target, path, 0, res)
        return res
    
    def dfs(self, candidates, k, target, path, begin, res):
        if len(path) == k and target == 0:
            res.append(path[:])
        
        for index in range(begin, len(candidates)):
            if len(path) > k:
                break
                
            path.append(candidates[index])
            self.dfs(candidates, k, target-candidates[index], path, index+1, res)
            path.pop()
            
# Time: O(K * (2^N))
# Space: O(K * (2^N))                
            
    
# Method 2: sorting and pruning less
class Solution(object):
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        res = []
        path = []
        self.dfs(candidates, k, target, path, 0, res)
        return res
    
    def dfs(self, candidates, k, target, path, begin, res):
        if len(path) == k and target == 0:
            res.append(path[:])
        
        if len(path) > k:
            return
        
        for index in range(begin, len(candidates)):
            path.append(candidates[index])
            self.dfs(candidates, k, target-candidates[index], path, index+1, res)
            path.pop()
            
# Time: O(K * (2^N))
# Space: O(K * (2^N))     