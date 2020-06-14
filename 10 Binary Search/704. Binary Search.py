class Solution:
    def search(self, li: List[int], target: int) -> int:
        # (0) edge case
        if len(li) == 0:
            return -1
        
        # (1) two pointers and while loop
        l, r = 0, len(li)-1
        while l <= r:                        # why l <= r? stop when left pointer is on the right of right pointer
            mid = (l + r) // 2
            if li[mid] == target:
                return mid
            elif li[mid] < target:
                l = mid + 1
            elif li[mid] > target:
                r = mid - 1
        
        # (2) otherwise return -1
        return -1

# Time: O(logn)
# Space: O(1)

    
class Solution:
    def search(self, li: List[int], target: int) -> int:
        # (0) edge case
        if len(li) == 0:
            return -1
        
        # (1) two pointers and while loop
        l, r = 0, len(li)-1
        while l+1 < r:                      # why l+1<r? stop when lr or (lr)
            mid = (l + r) // 2
            if li[mid] == target:
                return mid
            elif li[mid] < target:
                l = mid                     # if mid needs to add 1 or not depends on li[mid] =? target
            elif li[mid] > target:
                r = mid
        
        # (2) check boundary condition
        if li[l] == target:                 # used to judge len(1) or len(2)
            return l
        if li[r] == target:
            return r
        
        # (3) otherwise return -1
        return -1
    
# Time: O(logn)
# Space: O(1)