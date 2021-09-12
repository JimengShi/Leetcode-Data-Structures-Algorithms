class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        temp_count = 1
        max_count = 1
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp_count += 1
                max_count = max(max_count, temp_count)
            else:
                temp_count = 1
                
        return max_count

    

# SIMILAR question: find the length of the longest substring with the repeating letter 

# class Solution:
#     def findLengthOfLongestSubstring(self, s):    
#         cur_count = 1
#         max_count = 0

#         for i in range(len(s)-1):
#             if s[i] == s[i+1]:
#                 cur_count += 1
#                 max_count = max(max_count, cur_count)
#             else:
#                 cur_count = 1

#         return max_count

    
# # s = 'ABBBBBABA'
# # s = '101101111'
    
# Time: O(N), where N is the length of nums. We perform one loop through nums.
# Space: O(1), the space used by result and count.
