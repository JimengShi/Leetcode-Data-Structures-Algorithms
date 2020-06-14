class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # (1) initialize data structure
        dic = {}
        
        # (2) traverse given array
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:  # case 1: same element comes up and check difference of their indices
                return True
            dic[v] = i                        # case 2: different elements comes up
            
        # (3) otherwise return False
        return False
    
# Time: O(N)
# Space: O(1)