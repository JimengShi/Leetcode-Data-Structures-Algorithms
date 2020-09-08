# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
    
# Time: O(nlogn+mlogm), where n and m are arrays' lengths.
# Space: O(min(m,n)) in the worst case all elements are different.


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        dict1 = dict()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
                
        res = []
        for i in nums2:
            if i in dict1 and dict1[i] > 0:     # control duplicate with val in (key, val)
                res.append(i)
                dict1[i] -= 1
        return res
    
# Time: O(m+n), where n and m are arrays' lengths.
# Space: O(min(m,n)) in the worst case all elements are different.


# dict1[i] > 0
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# res = [9,4,9,4]