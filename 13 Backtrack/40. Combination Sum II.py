# Method 1: sorting and pruning
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, begin, path, res):                           
        if target == 0:                                     # 如果不先copy，那么append到res中到path也会随着path的变换而变化
            res.append(path[:])
            return

        for index in range(begin, len(candidates)):
            if index > begin and candidates[index-1] == candidates[index]:  # 对于重复数值，只让第一个进入循环，后面的就不要再进了
                continue                                                    # [1,2,2,3]: the second 2 would be skipped
                
            temp = target - candidates[index]
            
            if temp < 0:                                                    # 剪枝
                break
            
            path.append(candidates[index])
            self.dfs(candidates, temp, index+1, path, res)                  # index+1
            path.pop()

# 作者：allen-238
# 链接：https://leetcode-cn.com/problems/combination-sum-ii/solution/xiang-xi-jiang-jie-ru-he-bi-mian-zhong-fu-by-allen/


# Time: O(K * (2^N))
# Space: O(K * (2^N))



# Method 2: sorting and pruning less
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
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
            if index > begin and candidates[index] == candidates[index-1]:  # 对于重复数值，只让第一个进入循环，后面的就不要再进了
                continue
                
            path.append(candidates[index])
            self.dfs(candidates, index+1, target-candidates[index], path, res) 
            path.pop()