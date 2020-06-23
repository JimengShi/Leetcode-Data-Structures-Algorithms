# Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of given array must be used to form the two numbers.

# Input: [6, 8, 4, 5, 2, 3]
# Output: 604
# The minimum sum is formed by numbers 358 and 246

# Input: [5, 3, 0, 7, 4]
# Output: 82
# The minimum sum is formed by numbers 35 and 047

# Method 1: sort
def minSum(nums):
    nums.sort()                                # min-heap: [6, 8, 4, 5, 2, 3] --> [2, 3, 4, 5, 6, 8]
    num1 = 0
    num2 = 0
    for i in range(len(nums)):
    	if i % 2 == 0:
        	num1 = num1 * 10 + nums[i]
        else:
            num2 = num2 * 10 + nums[i]
    
    return num1 + num2

# Time: O(NlogN)
# Space: O(1)


# Method 2: heap
import heapq
def minSum(nums):
    heapq.heapify(nums)                                # min-heap: [6, 8, 4, 5, 2, 3] --> [2, 3, 4, 5, 6, 8]
    num1 = 0
    num2 = 0
    while nums:
        num1 = num1 * 10 + heapq.heappop(nums)         # greedy: from small to big
        if nums:
            num2 = num2 * 10 + heapq.heappop(nums)
    
    return num1 + num2


# Time: O(NlogN)
# Space: O(1)