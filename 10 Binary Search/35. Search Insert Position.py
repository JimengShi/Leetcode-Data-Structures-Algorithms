class Solution(object):
    def searchInsert(self, li, target):
        # (0) edge case
        if len(li) == 0:
            return -1

        # (1) two pointers and while loop
        l, r = 0, len(li)-1
        while l+1 < r:
            mid = (l+r) // 2
            if li[mid] == target:
                return mid
            if li[mid] < target:
                l = mid
            else:
                r = mid
        
        # (2) check boundary condition when r is the next to l
        if li[l] >= target:      # find the 1st element which is >= target
            return l
        if li[r] >= target:
            return r

        # (3) otherwise return r+1
        return r+1