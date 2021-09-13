### Q53, 209, 560, 930

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result, total, hmap = 0, 0, {}
        for num in nums:
            hmap[total] = hmap.get(total,0) + 1
            total += num
            if hmap.get(total-k):
                result += hmap[total-k]
        return result

    

class Solution:
    def subarraySum(self, nums, k):
        sumDict = {0:1}
        n = len(nums)
        count = 0 
        s = 0 

        for num in nums:                # keep adding to the cumilative sums, s:         
            s += num
            
            if s-k in sumDict:          # check if sum-k is already in dictionary, if so, increase count
                count += sumDict[s-k]
                           
            sumDict[s] = sumDict.get(s, 0) + 1 # check if s is already in sumDict, if so, increase by 1, if not assign 1.
#             else:
#                 sumDict[s] = 1
        
        return count

        
# first we start from a sum which is equal to 0, and the count of it is 1. 
# this is the input list ex :   [1 4 9 -5 8]
# this is the sum array (s) ex : [0  1    5    13    8    16 ]  


    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:  
        # (0) edge case
        if not nums:
            return 0
        
        # (1) initialize a dic and count
        dic = { 0: 1 }
        count = res = 0
        
        # (2) traverse nums
        for i, num in enumerate(nums):
            if num % 2 == 1:                     # (2.1) count odd number
                count += 1

            if count - k in dic:                 # (2.2) accumulatively res if count-k in dic
                res += dic[count-k]

            dic[count] = dic.get(count, 0) + 1
        
        # (3) return result
        return res
    
    
    
# This method is not working for this question, because sliding window is suitable for the list without negative values, e.g., Q209, 930.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if sum(nums) != k:
            return 
        cur_sum = 0
        count = 0
        total_num = 0
        l = 0
        
        for r in range(len(nums)):
            cur_sum += nums[r]
            if nums[r] != 0:
                count = 0
            while l <= r and cur_sum = k:
                if cur_sum == k:
                    count += 1
                cur_sum -= nums[l]
                l += 1
            total_num += count
        return total_num
    
