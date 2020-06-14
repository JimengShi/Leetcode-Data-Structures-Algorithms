class Solution(object):
    def search(self, nums, target):
        # (0) edge case
        if len(nums) == 0:
            return -1

        # (1) two pointers and while loop
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:                            # left to mid is sorted ascending
                if nums[l] <= target and target <= nums[mid]:  # li[l] <= target <= li[mid]
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid
                else:
                    r = mid
        
        # (2) check boundary condition
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        # (3) otherwise return -1
        return -1
    
# Time: O(logn)
# Space: O(1)