# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:
# Input: [1,2,3]
# Output: 6

# Example 2:
# Input: [1,2,3,4]
# Output: 24


# Algorithm:
# nums.sort()
# case 1: First three largest positive numbers (+++)
# case 2: First two smallest negative numbers (absolute value bigger), with one largest positive number (+--)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:      
        nums.sort()
        
        candidate_1 = nums[-1] * nums[-2] * nums[-3]       # like: [  1,  2, 3, 4, 5, 7]
        candidate_2 = nums[-1] * nums[0] * nums[1]         # like: [-10, -9, 1, 2, 5, 7] 
        max_product = max( candidate_1, candidate_2)
        
        return max_product
    
# Time: O(NlogN)
# Space: O(1)



class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        smallest = [float('inf')] * 2      # find first two smallest numbers
        largest = [float('-inf')] * 3      # find first three largest numbers
        
        for num in nums:
            if num <= smallest[0]:
                smallest[0] = num
                smallest.sort(reverse=True)
                
            if num >= largest[0]:
                largest[0] = num
                largest.sort()

        return max(smallest[0]*smallest[1]*largest[2], largest[0]*largest[1]*largest[2])
    
    
# Time: O(N)
# Space: O(1)