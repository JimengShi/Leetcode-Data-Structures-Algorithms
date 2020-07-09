# Method 1: Cumulative Sum
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # (0) edge case
        if not nums:
             return 0
            
        # (1) initialize a P array with 0
        P = [0]
        
        # (2) cummulative sum
        for x in nums:
            P.append(P[-1] + x)
        
        # (3) get the maximum moving_sum
        moving_sum = max(P[i+k] - P[i] for i in range(len(nums) - k + 1))
        
        # (4) return result
        return moving_sum / float(k)
    
#    [1, 12,-5,-6, 50, 3], k = 4
# [0, 1]
# [0, 1, 13]
# [0, 1, 13, 8]
# [0, 1, 13, 8, 2]
# [0, 1, 13, 8, 2, 52]
# [0, 1, 13, 8, 2, 52, 55]
    
# Time: O(n). We iterate over the nums array of length n once to fill the sum array. Then, we iterate over n−k elements of sum to determine the required result.
# Space: O(n). We make use of a sum array of length n to store the cumulative sum.



# Method 2: Sliding Window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # (0) edge case
        if not nums:
            return 0
        
        # (1) initialize moving_sum and calculate the sum of first k elements
        moving_sum = 0.0
        for i in range(k):
            moving_sum += nums[i]
        
        # (2) calculate the moving_sum by sliding window
        res = moving_sum
        for i in range(k, len(nums)):
            moving_sum += nums[i] - nums[i - k]
            res = max(res, moving_sum)
            
        # (3) return result
        return res / k
    
# Time: O(n). We iterate over the given nums array of length nn once only.
# Space: O(1). Constant extra space is used.