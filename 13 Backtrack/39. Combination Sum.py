# Method 1: sorting and pruning more
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # (1) edge case
        if len(candidates) == 0:
            return []

        # (2) sorting is the base of pruning, because the number in the next level should be > number in the previous level
        candidates.sort()
        path = []                            # record path when traversing
        res = []
        self.dfs(acandidates, 0, path, res, target)
        
        # (3) return result
        return res

    
    def dfs(self, candidates, begin, path, result, target):
        if target == 0:
            result.append(path[:])            # Python 中可变对象是引用传递，因此将当前 path 里的值拷贝出来，使用 path.copy()
            return

        for index in range(begin, len(candidates)):
            residue = target - candidates[index]
            
            if residue < 0:                   # prunig: don't have to recurse next level and next branches because it's sorted
                break
                
            path.append(candidates[index])
            self.dfs(candidates, index, path, result, residue)   # recursion
            path.pop()

# Time: O(N * (2^N))
# Space: O(K * (2^N))
            
    
# Method 2: no sorting and pruning less
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        res = []
        path = []                            
        self.dfs(candidates, 0, target, path, res)
        return res
    
    
    def dfs(self, candidates, begin, target, path, res):
        if target == 0:                       
            res.append(path[:])
            return
            
        if target < 0:
            return
        
        for index in range(begin, len(candidates)):
            path.append(candidates[index])
            self.dfs(candidates, index, target-candidates[index], path, res) 
            path.pop()


# Time: O(K * (2^N))
# Space: O(K * (2^N))
# 遇到 0 就结算且回溯，遇到负数也回溯。