# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2


class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
# Time: O(nlgn)
# Space: O(1) or O(n) which depends on if we want to save the sorted list


from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for k,v in count.items():
            if v > len(nums)//2:
                return k
        return -1

# Time: O(n)
# Space: O(n)
    
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for k, v in d.items():
            if v > len(nums)//2:
                return k
            
        return -1   
    
# Time: O(n)
# Space: O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        for k, v in d.items():
            if v > len(nums)//2:
                return k
            
        return -1
      
# Time: O(n)
# Space: O(n)