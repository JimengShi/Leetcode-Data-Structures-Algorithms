class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)             # False: not traversed; True: traversed

        def dfs(nums, temp):
            if len(temp) == len(nums):
                res.append(temp[:])

            for i in range(len(nums)):
                if used[i]:                    # condition 1: use[i] = True means curr is traversed --> skip
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == True:   # condition 2: repeat and last is used
                    continue
                    
                used[i] = True
                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()
                used[i] = False
                
        dfs(sorted(nums), [])
        return res
    
# Why we set condition 2?
# If we do not set condition 2, the final output would be [[1,1,2],[1,2,1],[1,1,2],[1,2,1],[2,1,1],[2,1,1]] which can be considered as the output of Problem 46. In other words, the second 2 is considered it's different with the first 1. Therefore there is a double here. The solution to solve this is we need to skip the second 1 when we have already used the first 1.


# Time: O(N x N!). Initially we have N choices, and in each choice we have (N - 1) choices, and so on. Notice that at the end when adding the list to the result list, it takes O(N).
# Space：O(N x N!). Since we have N! solutions and each of them requires N space to store elements. 