# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# Unique permutations means we only use each element of input once.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # used = [False] * len(nums)
        
        def dfs(nums, temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue

                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()
                
        dfs(nums, [])
        return res
    
    
# Time: O(N x N!). Initially we have N choices, and in each choice we have (N - 1) choices, and so on. Notice that at the end when adding the list to the result list, it takes O(N).
# Space：O(N x N!). Since we have N! solutions and each of them requires N space to store elements.    


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        
        def dfs(nums, temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()
                used[i] = False
                
        dfs(nums, [])
        return res
    
# Time: O(N x N!). Initially we have N choices, and in each choice we have (N - 1) choices, and so on. Notice that at the end when adding the list to the result list, it takes O(N).
# Space：O(N x N!). Since we have N! solutions and each of them requires N space to store elements.  


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, temp, res):
        if len(temp) == len(nums):
            res.append(temp[:])
            return

        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.dfs(nums, temp, res)
            temp.pop()
            
# Time: O(N x N!). Initially we have N choices, and in each choice we have (N - 1) choices, and so on. Notice that at the end when adding the list to the result list, it takes O(N).
# Space：O(N x N!). Since we have N! solutions and each of them requires N space to store elements.  