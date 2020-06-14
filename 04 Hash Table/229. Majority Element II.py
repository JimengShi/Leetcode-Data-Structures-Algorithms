# Method 1:
class Solution(object):
    def majorityElement(self, nums):
        # (0) edge case
        if len(nums) < 3:
            return list(set(nums))
        
        # (1) maintain a list and count the times each element appears
        res = []
        for x in set(nums):
            t = nums.count(x)
            if t > len(nums)//3:
                res.append(x)

        # (2) return result
        return res
    
# Time: O(n)
# Space: O(n)
    
    
# Method 2:    
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)
        res = []
        for k,v in count.items():
            if v > len(nums)//3:
                res.append(k)
        return res

# Time: O(n)
# Space: O(n)    



# Method 3:
# Since the number of majority element that appears more than ⌊ n/2 ⌋ times at most 2.
# Therefore, we maintain a dictionary to save two candidates.
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        ctr = Counter()
        for n in nums:
            ctr[n] += 1
            # only save the two elements that appear the most by decreasing time once of each element
            if len(ctr) > 2:
                ctr -= Counter(set(ctr)) 
                
        res = []       
        for n in ctr:
            if nums.count(n) > len(nums)/3:
                res.append(n)
        return res
    
# Time: O(n)
# Space: O(1)

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# Counter({1: 1})
# Counter({1: 2})
# Counter({1: 3})
# Counter({1: 3, 3: 1})
# Counter({1: 3, 3: 2})
# Counter({1: 3, 3: 2, 2: 1})
# reduce:  Counter({1: 2, 3: 1})
# Counter({1: 2, 3: 1, 2: 1})
# reduce:  Counter({1: 1})
# Counter({1: 1, 2: 1})
# [1, 2]
