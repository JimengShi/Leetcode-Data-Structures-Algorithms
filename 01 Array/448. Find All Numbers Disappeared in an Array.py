# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


# Method 1: Dictionary or set
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # (1) Hash table, we can also use a set since we are not concerned with the frequency of numbers
        hash_table = {}

        # (2) Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        
        # (3) Initialize an empty array, and travers 1...N to find the missing numbers
        result = []    
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
        
        # (4) return the result
        return result

# Time: O(n)
# Space: O(n)


# Method 2: In place
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # (1) Iterate over each of the elements in the original array
        for i in range(len(nums)):
            home_index = abs(nums[i]) - 1
            if nums[home_index] > 0:
                nums[home_index] *= -1
        
        # (2) Initialize an list to contain the missing numbers
        result = []    
        
        # (3) Iterate over the numbers from 1 to N and add all those that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i-1] > 0:
                result.append(i)
                
        # (4) return result
        return result
    
# Time: O(n)
# Space: O(1)