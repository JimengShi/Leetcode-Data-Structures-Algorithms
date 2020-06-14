# Basic idea is that, If you get the same remainder again, it means that you've encountered some sum which is a multiple of K.
# original d: {0: -1}
# i: 0
# nums: 23
# sums: 23
# remainder: 5
# new d: {0: -1, 5: 0}
# -----------------
# i: 1
# nums: 2
# sums: 7
# remainder: 1
# new d: {0: -1, 5: 0, 1: 1}
# -----------------
# i: 2
# nums: 4
# sums: 5
# remainder: 5, when we encount remainder is 5 again, so we find a subarray sums up to a multiple of k
# True

# k = 2
# 3 % 2 = 1
# 7 % 2 = 1
# 9 % 2 = 1
# (9-3) % 2 == 0 differnce must be divided by 2

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # (0) maintain a dictionary and edge case
        d = dict()
        d[0] = -1
        
        # (1) initialize sum = 0 and get accumlative sum
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]          
            if k != 0:
                sums = sums % k      # (1.1) get remainder when k != 0
                
            if sums in d:
                if i-d[sums] > 1:    # (1.2) check distance of index when remainder is in the dictionary
                    return True
            else:
                d[sums] = i          # (1.3) add the remainder into dictionary when it's not in there
        
        # (2) otherwise, return False
        return False
    

# Time: O(n)
# Space: O(n)