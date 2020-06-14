class Solution(object):
    def findPeakElement(self, alist):
        return self.peak_helper(alist, 0, len(alist) - 1)

    def peak_helper(self, alist, start, end):
        if start == end:
            return start

        if start + 1 == end:
            if alist[start] > alist[end]:
                return start
            return end

        mid = (start + end) // 2
        if alist[mid] > alist[mid - 1] and alist[mid] > alist[mid + 1]:
            return mid
        if alist[mid - 1] > alist[mid] and alist[mid] > alist[mid + 1]:
            return self.peak_helper(alist, start, mid - 1)
        
        return self.peak_helper(alist, mid + 1, end)
           

# Time: O(logn). We reduce the search space in half at every step. Thus, the total search space will be consumed in logn steps. Here, n refers to the size of numsnums array.
# Space: O(logn). We reduce the search space in half at every step. Thus, the total search space will be consumed in logn steps. Thus, the depth of recursion tree will go upto logn.
           
class Solution(object):
    def findPeakElement(self, nums):
        # edge case and boundary check
        if len(nums) < 2:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        
        # binary search
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2     
            # no need for bound checking since we already checked the first/last index at the beginning
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:                
                hi = mid - 1
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1
        return -1
    
# Time: O(logn). We reduce the search space in half at every step. Thus, the total search space will be consumed in logn steps. Here, n refers to the size of numsnums array.
# Space: O(1).