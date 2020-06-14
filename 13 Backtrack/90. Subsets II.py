class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(nums, temp, index):
            res.append(temp[:])

            for i in xrange(index, len(nums)):
                # Check for index bound, and remove duplicate
                if i > index and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()
        dfs(sorted(nums), [], 0)
        return res
    
# Time: O(N×2^N) to generate all subsets and then copy them into output list.
# Space: O(N×2^N) to keep all the subsets of length N, since each of N elements could be present or absent.