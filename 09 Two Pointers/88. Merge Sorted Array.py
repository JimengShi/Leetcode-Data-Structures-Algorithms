# Approach 1: Merge and sort
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)

# Time: O((n+m)log(n+m)).
# Space: O(1).
        
    
# Approach 2: Two pointers / Start from the beginning
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Make a copy of nums1.
        nums1_copy = nums1[:m] 
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1, p2 = 0, 0 
        
        # Compare elements from nums1_copy and nums2 and add the smallest one into nums1.
        while p1 < m and p2 < n: 
            if nums1_copy[p1] < nums2[p2]: 
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m: 
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
            
# Time: O(n+m).
# Space: O(m), Since nums1 is an array used for output, one has to keep first m elements of nums1 somewhere aside       


# Approach 3: Two pointers / Start from the end
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # two get pointers starting from the end of nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1       # set pointer for nums1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        
        # # only need to add missing elements from nums2, because missing nums have been in the nums list
        nums1[:p2 + 1] = nums2[:p2 + 1]

            
# Time: O(n+m).
# Space: O(1).