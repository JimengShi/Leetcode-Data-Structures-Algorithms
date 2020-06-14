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