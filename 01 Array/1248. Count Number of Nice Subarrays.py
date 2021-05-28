# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         # (0) edge case
#         if not nums:
#             return 0
        
#         # (1) initialize a dic and count
#         dic = { 0: 1 }
#         count = res = 0
        
#         # (2) traverse nums
#         for i, num in enumerate(nums):
#             if num % 2 == 1:                     # (2.1) count odd number
#                 count += 1

#             if count - k in dic:                 # (2.2) accumulatively res if count-k in dic
#                 res += dic[count-k]

#             dic[count] = dic.get(count, 0) + 1
        
#         # (3) return result
#         return res

    
# Time: O(n)
# Space: O(n) 


class Solution(object):
	def numberOfSubarrays(self, nums, k):
		odds = []
		for i in range(len(nums)):
			if nums[i] & 1:                         # odd number: nums[i] % 2 == 1
				odds.append(i)                      # Find index of all odd numbers

		odds = [-1] + odds + [len(nums)]            # Handle edge cases
		
        nice = 0

		for i in range(1, len(odds)-k):
			left = odds[i] - odds[i-1] - 1          #' Number of 'left' even numbers '
			right = odds[i+k] - odds[i+k-1] - 1     #' Number of 'right' even numbers '
			nice += (left+1)*(right+1)              #' Total sub-arrays in current window '

		return nice

# Time: O(n)
# Space: O(n)