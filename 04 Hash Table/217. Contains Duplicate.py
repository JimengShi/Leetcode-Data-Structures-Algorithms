class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for n in nums:
            if n in dic: 
                return True
            else: 
                dic[n] = 1
        return False
    
# Time: O(N)
# Space: O(1)


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
# Time: O(NlogN)
# Space: O(1)