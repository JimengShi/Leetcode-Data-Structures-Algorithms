# Method 1: linear scan
class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost target. if it does not appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost target (by reverse iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

# Time: O(n)
# Space: O(1)
    
    
# Method 2: binary search    
class Solution(object):
    def searchRange(self, li, target):
        # (0) edge case
        if len(li) == 0:
            return (-1, -1)
        
        # (1) initialize left and right boundary
        lbound, rbound = -1, -1

        # (2) search for left bound
        l, r = 0, len(li)-1
        while l+1 < r:
            mid = (l+r) // 2
            if li[mid] == target:
                r = mid
            elif li[mid] < target:
                l = mid
            else:
                r = mid
                
        if li[r] == target:            # check li[r] first, then li[l] because we want to get the leftmost index
            lbound = r
        if li[l] == target:
            lbound = l
        
        # (3) search for right bound
        l, r = 0, len(li)-1
        while l+1 < r:
            mid = (l+r) // 2
            if li[mid] == target:
                l = mid
            elif li[mid] < target:
                l = mid
            else:
                r = mid

        if li[l] == target:            # check li[l] first, then li[r] because we want to get the rightmost index
            rbound = l
        if li[r] == target:
            rbound = r
        
        # (4) return result
        return (lbound, rbound)
    
# Time: O(logn)
# Space: O(1)