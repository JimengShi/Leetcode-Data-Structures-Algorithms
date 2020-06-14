class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # (1) initialize data structure
        stack = []
        unordered_map = {}
        
        # (2) traverse nums2 to find the next greater element
        for curr in nums2:
            while stack and curr > stack[-1]:
                unordered_map[stack[-1]] = curr
                stack.pop()
            stack.append(curr)

        # (3) traverse nums1 to find the next greater element
        res = []
        for j in nums1:
            if j in unordered_map:
                res.append(unordered_map[j])
            else:
                res.append(-1)
                
        # (4) return result
        return res
    
# Time: O(M+N)    
# Space: O(M+N)
    
    
# Similar question    
# array = [6, 4, 5, 2, 25]
# 4 :  5
# 2 :  25
# 5 :  25
# 6 :  25
# 25 : -1    
# for i in range(1, len(nums)):
#     while (len(stack) != 0 and nums[i] > stack[-1]):
#         num = stack.pop()
#         print(num, ": ", array[i])
#     stack.append(nums[i])

# while len(stack) != 0:
#     print(stack.pop(), ": -1")