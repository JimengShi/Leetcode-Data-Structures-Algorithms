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