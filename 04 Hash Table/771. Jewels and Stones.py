class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for c in S:
            if c in J:
                count += 1
        return count
    
# Time: O(N)
# Space: O(1)